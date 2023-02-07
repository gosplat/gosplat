package main

import (
	"fmt"
	"os"

	"github.com/Gabriel-Ivarsson/code2vec-demo/tool/src/ToolParser"
)

func main() {
	dir := os.Args[1]
	astParser.ParseDir(dir)
	return
}
