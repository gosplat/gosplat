// Package toolParser ,package for dealing with parsing and testing of files
//
// file for dealing with parsing of directory
package toolParser

import (
	"go/ast"
	"regexp"
	"strings"
)

var (
	funcType    = "funcDecl"
	packageType = "package"
)

func sanitizeName(name string) string {
	name = strings.ToLower(name)
	name = regexp.MustCompile(`[^a-zA-Z0-9 ]+`).ReplaceAllString(name, "")
	return name
}

func parseCode(newPackage *projectPackage, node *ast.File) {
	file := newPackage.Files[len(newPackage.Files)-1]

	ast.Inspect(node, func(n ast.Node) bool {
		switch x := n.(type) {
		case *ast.FuncDecl:
			file.Functions = append(file.Functions, sanitizeName(x.Name.Name))
		}

		return true
	})
}
