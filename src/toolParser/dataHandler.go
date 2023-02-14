// Package toolParser ,package for dealing with parsing and testing of files
//
// file for dealing with parsing of directory
package toolParser

import (
	"encoding/json"
	"go/ast"
	"regexp"
	"strings"
)

type projectPackage struct {
	Name      string   `json:"package_name"`
	Functions []string `json:"functions"`
}

var packages = make(map[string]*projectPackage)

func sanitizeName(name string) string {
	name = strings.ToLower(name)
	name = regexp.MustCompile(`[^a-zA-Z0-9 ]+`).ReplaceAllString(name, "")
	return name
}

func getPackageName(node *ast.File) string {
	return sanitizeName(node.Name.Name)
}

func getMapPackage(key string) *projectPackage {
	if val, ok := packages[key]; ok {
		return val
	}
	newPackage := projectPackage{
		Name: key,
	}
	packages[key] = &newPackage
	return &newPackage
}

// GenerateInputJSON function
func GenerateInputJSON() (string, error) {
	jsonData, err := json.Marshal(packages)
	if err != nil {
		return "", err
	}
	return string(jsonData), nil
}
