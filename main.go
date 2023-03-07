// main package
package main

import (
	"fmt"
	"os"

	"github.com/NoahHakansson/gosplat/src/pythonRunner"
	"github.com/NoahHakansson/gosplat/src/toolParser"
)

func printHelp() {
	fmt.Printf("Gosplat v1\n" +
		" gosplat -h/--help , prints this help text\n" +
		" gosplat [input dir/file] , runs directory against model\n")
}

func checkForFlags(args []string) uint8 {
	if len(args) == 1 {
		printHelp()
		return earlyReturn
	}
	for _, arg := range args {
		if arg == "-h" || arg == "--help" {
			printHelp()
			return earlyReturn
		}
	}
	return continueProgram
}

var (
	pythonPath = os.Getenv("HOME") + "/.local/share/gosplat/src/python_helper/fast_model_compare.py"
	modelBin   = os.Getenv("HOME") + "/.local/share/gosplat/fast-fb-model.bin"
)

const (
	earlyReturn     uint8 = 1
	continueProgram uint8 = 2
)

func main() {
	if checkForFlags(os.Args) == earlyReturn {
		return
	}
	dir := os.Args[1]
	if _, err := os.Stat(dir); os.IsNotExist(err) {
		fmt.Println("Error; Input was not a directory or file")
		printHelp()
		return
	}
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
