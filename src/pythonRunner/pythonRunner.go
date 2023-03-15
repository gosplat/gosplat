// Package pythonrunner provides pythonrunner
package pythonrunner

import (
	// "fmt"
	"os"
	"os/exec"
	"strconv"
)

// ExecPythonModel function
func ExecPythonModel(path string, modelFile string, jsonData string, accuracy int, nameSuggestion bool) error {
	accuracyStr := strconv.Itoa(accuracy)
	var nameSuggestionStr string
	if nameSuggestion {
		nameSuggestionStr = "1"
	} else {
		nameSuggestionStr = "0"
	}
	cmd := exec.Command("python3", path, modelFile, "-j", jsonData, "-a", accuracyStr, "-ns", nameSuggestionStr)
	// fmt.Printf("\nExecuted command: %s\n\n", cmd.String())
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil {
		return err
	}
	return nil
}
