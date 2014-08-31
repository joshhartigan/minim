// Name:        minim.go
// Author:      Josh Hartigan
// Description: Interpreter (not REPL) for Minim programming language.

package main

import (
	"bufio"
	"fmt"
	"github.com/joshhartigan/minim/lang"
	"os"
)

func main() {
	if len(os.Args) > 2 {
		fmt.Println("*** Minim: too many arguments")
		os.Exit(1)
	} else if len(os.Args) < 2 {
		fmt.Println("*** Minim: no file specified")
	} else {
		processLines(getLines(os.Args[1]))
	}
}

// getLines opens a file from the filename passed
// as an argument to it, and returns an array that
// holds each line of the file.
func getLines(filename string) (lines []string) {
	source, err := os.Open(filename)
	defer source.Close()
	check(err, "*** Minim: source file is non-existant")

	scanner := bufio.NewScanner(source)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return
}

func processLines(lines []string) {
	for _, line := range lines {
		if len(line) != 0 {

			if lang.IsNumber(line) {
				fmt.Println(line, "is a number")
			} else if lang.IsOperator(line) {
				fmt.Println(line, "is an operator")
			} else if lang.IsExpression(line) {
			} else if lang.IsFunctionCall(line) {
			} else {
				fmt.Println("*** Minim:", line, "is an unrecognizable statment")
			}

		}
	}
}

// check simply checks for an error, and responds
// if an error occurs.
func check(e error, msg string) {
	if e != nil {
		fmt.Println(msg)
	}
}
