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
	flag.IntVar(&accuracy, "a", 1, `Accuracy; The hit rate of errors, (1 is high - 10 low)`)
	flag.BoolVar(&nameSuggestions, "ns", false, "Name suggestions; If error occurs, suggest a better name for package")
	flag.Parse()
	if _, err := os.Stat(dir); os.IsNotExist(err) {
		fmt.Printf("Error; Input was not a directory or file\n\n")
		flag.PrintDefaults()
		log.Fatal("Error; Given directory does not exist")
	}
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
