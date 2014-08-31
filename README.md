![Minim](http://joshhartigan.github.io/minim/logo.png)

Minim is an interpreted programming language being written in Go. There are two previous
attempts of writing the interpreter in Python and C++. The interpreter,
`mi`, reads a plain text file (extension .min) and evaluates it line by line.

### Minim Interpter v2.5.0 [mi25] Checklist:

#### Completed:

  * mi25 recognises numbers
  * mi25 recognises operators ("/", "*", "+", "-")
  * mi25 recognises expressions (e.g. "3 + 8 * 2")
  * mi25 recognises calls for functions from the standard library
  
#### Incomplete / In Progress

  * mi25 runs functions from the standard library when called
  * mi25 can evaluate expressions
  * mi25 can define and recall variables

### Syntax

This program writes 'Hello, World' 10 times.

  ```
  var i = 0
  for i++ until 10 {
    (write "Hello, World")
  }
  ```

An explanation of syntactical elements shown above:

  * Dynamic typing with `var` keyword
  * Emphasis on readability:
    * *C++* `for` statement header: `for (int i = 0; i < 10; i++)`
    * *Minim* `for` statement header: `for i++ until 10`
  * Function calls follow syntax `(functionName param1 param2 ...)`
  * Blocks defined by braces - insignificant whitespace.


### Freedom

Licensed under the MIT License - see 'LICENSE' file for details.
