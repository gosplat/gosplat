// Package toolParser ,package for dealing with parsing and testing of files
//
// file for dealing with parsing of directory
package toolParser

import (
	"encoding/json"
	"go/ast"
)

type projectPackage struct {
	Functions []string `json:"functions"`
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
