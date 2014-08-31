// Name:        library / functions.go
// Author:      Josh Hartigan
// Description: Standard libary functions for Minim.

package lang

import (
	"fmt"
	"strings"
)

var functionNames = []string{
	"write",   // print to standard output
	"writeln", // print to standard output with \n
	"power",   // raise first parameter to second paramater's power
}

func IsStdLibFunction(str string) bool {
	for _, s := range functionNames {
		if s == str {
			return true
		}
	}
	return false
}

func Call(function string, params []string) {
	switch function {
	case functionNames[0]: // write
		write(params, false)
	case functionNames[1]: // writeln
		write(params, true)
	case functionNames[2]: // power
		// TODO(joshhartigan): Implement Function
	}
}

// Begin StdLib Function Definitions //

func write(params []string, newline bool) {
	for _, p := range params {
		if IsString(p) {
			fmt.Println("NO")
		}
	}

	toPrint := strings.Join(params, " ")         // form one string from params
	toPrint = strings.TrimPrefix(toPrint, "\"")  // remove " from beginning
	toPrint = strings.TrimSuffix(toPrint, "\")") // remove leading ") from end

	if newline {
		fmt.Println(toPrint)
	} else {
		fmt.Print(toPrint)
	}
}
