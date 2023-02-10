// Package toolParser ,package for dealing with parsing and testing of files
//
// file for dealing with parsing of directory
package toolParser

import (
	"encoding/json"
	"go/ast"
)

type packageFiles struct {
	Name      string   `json:"filename"`
	Functions []string `json:"functions"`
}

type projectPackage struct {
	Files []*packageFiles `json:"package_files"`
}

var packages = make(map[string]*projectPackage)

func getPackageName(node *ast.File) string {
	return node.Name.Name
}

func getMapPackage(key string) *projectPackage {
	if val, ok := packages[key]; ok {
		return val
	}
	newPackage := projectPackage{}
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
