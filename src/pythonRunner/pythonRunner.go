// Package pythonrunner provides pythonrunner
package pythonrunner

import (
	"fmt"
	"os/exec"
)

func surroundInQuotes(jsonData string) string {
	return fmt.Sprintf("'%s'", jsonData)
}

// ExecPythonModel function
func ExecPythonModel(path string, modelFile string, jsonData string) error {
	cmd := exec.Command("python", path, modelFile, "-j", surroundInQuotes(jsonData))
	fmt.Printf("\nexec cmd: %s\n\n", cmd.String())
	out, err := cmd.Output()
	if err != nil {
		return err
	}
	fmt.Printf("Python output:\n%s", out)
	return nil
}
