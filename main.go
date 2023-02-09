// main package
package main

import (
	"fmt"
	"os"

	"github.com/NoahHakansson/go-slat/src/toolParser"
)

func main() {
	dir := os.Args[1]
	toolParser.ParseDir(dir)
	jsonData, err := toolParser.GenerateInputJSON()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Print(jsonData)
	return
}
