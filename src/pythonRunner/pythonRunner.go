// Package pythonrunner provides pythonrunner
package pythonrunner

import (
	// "fmt"
	"os"
	"os/exec"
)

// ExecPythonModel function
func ExecPythonModel(path string, modelFile string, jsonData string) error {
	cmd := exec.Command("python3", path, modelFile, "-j", jsonData)
	// fmt.Printf("\nExecuted command: %s\n\n", cmd.String())
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil {
		return err
	}
	return nil
}
