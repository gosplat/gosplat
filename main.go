// main package
package main

import (
	"fmt"
	"os"

	"github.com/NoahHakansson/gosplat/src/pythonRunner"
	"github.com/NoahHakansson/gosplat/src/toolParser"
)

var (
	pythonPath = os.Getenv("HOME") + "/.local/share/gosplat/src/python_helper/fast_model_compare.py"
	modelBin   = os.Getenv("HOME") + "/.local/share/gosplat/fast-fb-model.bin"
)

func main() {
	dir := os.Args[1]
	toolParser.ParseDir(dir)
	jsonData, err := toolParser.GenerateInputJSON()
	if err != nil {
		fmt.Println(err)
		return
	}
	err = pythonrunner.ExecPythonModel(pythonPath, modelBin, jsonData)
	if err != nil {
		println("ExecPythonModel; Error;", err.Error())
	}
	return
}
