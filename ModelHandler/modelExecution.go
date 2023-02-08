// modelHandler package
package modelHandler

import (
	"os/exec"
)

// ExecModel function
func ExecModel(jsonData string) error {
	model := exec.Command("compare.py", "-j", jsonData)
	if err := model.Run(); err != nil {
		return err
	}
	return nil
}
