// main package
package main

import (
	"fmt"
	"os"

	"github.com/NoahHakansson/gopslat/src/pythonRunner"
	"github.com/NoahHakansson/gopslat/src/toolParser"
)

func main() {
	dir := os.Args[1]
	toolParser.ParseDir(dir)
	jsonData, err := toolParser.GenerateInputJSON()
	if err != nil {
		fmt.Println(err)
		return
	}
	err = pythonrunner.ExecPythonModel("./python_helper/fastModelCompare.py", "./fast-fb-model.bin", jsonData)
	if err != nil {
		println("ExecPythonModel; Error;", err.Error())
	}
	return
}
