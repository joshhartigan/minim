// Name:        lang.go
// Author:      Josh Hartigan
// Description: Logic and brains for Minim

package lang

import "strings"

func Evaluate(expr string) int {
	// split into numbers and operands
	digits := "0123456789"

	for i, c := range expr {
		c := string(c)
		token := ""
		// if character is digit
		if strings.Contains(digits, c) {
			token += c
			for j := 1; strings.Contains(digits, string(expr[i+j])); j++ {
				token += string(expr[i+j])
			}
		}
	}
	//  opStack := [len(expr)]string{}
	return 0
}
