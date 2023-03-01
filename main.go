// main package
package main

import (
	"fmt"
	"os"

	"github.com/NoahHakansson/gosplat/src/pythonRunner"
	"github.com/NoahHakansson/gosplat/src/toolParser"
)

<<<<<<< HEAD
const (
	pythonPath = "/home/gabriel/.local/share/gosplat/src/python_helper/fast_model_compare.py"
	modelBin   = "/home/gabriel/.local/share/gosplat/fast-fb-model.bin"
=======

var (
	pythonPath = os.Getenv("HOME") + "/.local/share/gosplat/src/python_helper/fast_model_compare.py"
	modelBin   = os.Getenv("HOME") + "/.local/share/gosplat/fast-fb-model.bin"
>>>>>>> e6ee66556e2312f2b29179e6b578cd526984f31f
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
