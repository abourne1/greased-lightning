package main

import (
	"fmt"
	"os/exec"
)



func main() {
	fmt.Println("Hello, world!")
	cmd := exec.Command("sudo xboxdrv")
	cmd.StdoutPipe()
}
