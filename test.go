// Name:        test.go
// Author:      Josh Hartigan
// Description: Tools for testing Minim code.

package main

import (
	"fmt"
	"github.com/joshhartigan/minim/lang"
)

func testLine(line string) {
	fmt.Println() // for tidyness

	if lang.IsNumerical(line) {
		fmt.Println(line, "is a number")
	} else if lang.IsOperator(line) {
		fmt.Println(line, "is an operator")
	} else if lang.IsExpression(line) {
		fmt.Println(line, "is an expression")
	} else if lang.IsFunctionCall(line) {
	} else {
		fmt.Println("*** Minim:", line, "is an unrecognizable statment")
	}
}
