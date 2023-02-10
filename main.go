// main package
package main

import (
	"fmt"
	"os"

	pythonrunner "github.com/NoahHakansson/go-slat/src/pythonRunner"
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
	// TODO: call python fastTest model with jsonData string.
	fmt.Println("FROM GO PROGRAM: ", jsonData)
	err = pythonrunner.ExecPythonModel("test.py", "./fast-fb-model.bin", jsonData)
	if err != nil {
		println("ExecPythonModel; Error;", err.Error())
	}
	return
}
