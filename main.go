// main package
package main

import (
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/NoahHakansson/gosplat/src/pythonRunner"
	"github.com/NoahHakansson/gosplat/src/toolParser"
)

func printHelp() {
	fmt.Printf("Gosplat v1\n" +
		" gosplat -h/--help , prints this help text\n" +
		" gosplat [input dir/file] , runs directory against model\n")
}

var (
	pythonPath = os.Getenv("HOME") + "/.local/share/gosplat/src/python_helper/fast_model_compare.py"
	modelBin   = os.Getenv("HOME") + "/.local/share/gosplat/fast-fb-model.bin"
)

const (
	earlyReturn      uint8 = 1
	continueProgram  uint8 = 2
	accuracyOn       uint8 = 3
	nameSuggestionOn uint8 = 4
)

// flagValues
var (
	dir             string
	accuracy        int
	help            bool
	nameSuggestions bool
)

func checkForFlags() {
	flag.StringVar(&dir, "d", ".", "Directory; Dir which analysis starts on")
	flag.IntVar(&accuracy, "a", 1, "Accuracy; The amount of positives it reports on (not it will increase false positives)")
	flag.BoolVar(&nameSuggestions, "ns", false, "Name suggestions; if positive suggest a better name for package")
	if _, err := os.Stat(dir); os.IsNotExist(err) {
		fmt.Println("Error; Input was not a directory or file")
		printHelp()
		log.Fatal("Error; Given directory does not exist")
	}
	flag.Parse()
}

func main() {
	checkForFlags()
	toolParser.ParseDir(dir)
	jsonData, err := toolParser.GenerateInputJSON()
	if err != nil {
		fmt.Println(err)
		return
	}
	err = pythonrunner.ExecPythonModel(pythonPath, modelBin, jsonData, accuracy, nameSuggestions)
	if err != nil {
		println("ExecPythonModel; Error;", err.Error())
	}
	return
}
