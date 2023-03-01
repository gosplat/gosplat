// Package toolParser ,package for dealing with parsing and testing of files
//
// file for dealing with parsing of directory
package toolParser

import (
	"go/ast"
	"strings"
)

var (
	funcType    = "funcDecl"
	packageType = "package"
)

// Takes a ast node, finds and adds package functions to provided projectPackage struct
func parseCode(newPackage *projectPackage, node *ast.File) {
	ast.Inspect(node, func(n ast.Node) bool {
		switch x := n.(type) {
		case *ast.FuncDecl:
			funcName := x.Name.Name
			if strings.Contains(strings.ToLower(funcName), "test") ||
				strings.Contains(strings.ToLower(funcName), "mock") ||
				strings.Contains(strings.ToLower(funcName), "fixture") {
				// early return if function name starts with test,
				// we dont want to ignore all test functions.
				return true
			}
			newPackage.Functions = append(newPackage.Functions, funcName)
		}

		return true
	})
}
