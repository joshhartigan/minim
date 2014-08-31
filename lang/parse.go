// Name:        lang.go
// Author:      Josh Hartigan
// Description: Utilities for the Minim interpreter.

package lang

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

var oper = []string{"^", "*", "/", "+", "-"}

/**
 * IsSomething functions
 */

func IsOperator(str string) bool {
	for _, s := range oper {
		if s == str {
			return true
		}
	}
	return false
}

func IsNumerical(str string) bool {

	if strings.Contains(str, "sqrt") {
		str = strings.Replace(str, "sqrt", "", -1)
	}

	if _, err := strconv.Atoi(str); err == nil {
		return true
	}

	return false
}

func IsString(str string) bool {
	if (string(str[0]) == "\"" && string(str[len(str)-1]) == "\"") ||
		(string(str[0]) == "'" && string(str[len(str)-1]) == "'") {
		return true
	}
	return false
}

func IsExpression(line string) bool {
	expressives := 0
	tokens := strings.Fields(line)

	for i, token := range tokens {
		if i%2 != 0 && IsOperator(token) {
			expressives++
		} else if i%2 == 0 && IsNumber(token) {
			expressives++
		}
	}

	if expressives == len(tokens) {
		fmt.Println(Evaluate(line))
		return true
	}

	return false
}

func IsFunctionCall(line string) bool {
	if string(line[0]) != "(" && string(line[len(line)-1]) != ")" {
		return false
	}

	tokens := strings.Fields(line[1:len(line)])
	functionName := tokens[0]

	if IsStdLibFunction(functionName) {
		Call(functionName, tokens[1:])
		return true
	}

	return false
}

/**
 * Other functions
 */

func GetNumerical(str string) {
	if strings.Contains(str, "sqrt") {
		s := strings.Replace(str, "sqrt", "", -1)
		if n, err := strconv.Atoi(s); err == nil {
			return math.Sqrt(float64(n))
		}
	} else {
		if n, err := strconv.Atoi(s); err == nil {
			return n
		}
	}
}
