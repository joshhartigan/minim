#!/usr/local/bin/node

// Name:        minim.js
// Author:      Josh Hartigan
// Description: Central definitions for the Minim language.

var fs       = require("fs");
var evaluate = require("./evaluate");
var parser   = require("./parser");

// Special forms -- in a nutshell, reserved words.
exports.specialForms = Object.create(null);

exports.specialForms["if"] = function(args, env) {
  if (args.length != 3) {
    throw new SyntaxError("*** Insufficient args to `if` expression: " + args);
  }

  if ( evaluate.evalSyntax(args[0], env) !== false ) {
    return evaluate.evalSyntax( args[1], env );
  } else {
    return evaluate.evalSyntax( args[2], env );
  }
};

exports.specialForms["while"] = function(args, env) {
  if (args.length != 2) {
    throw new SyntaxError("*** Incorrect `while` expression: " + args);
  }

  while ( evaluate.evalSyntax( args[0], env ) !== false ) {
    evaluate.evalSyntax( args[1], env );
  }

  return false;
};

// this is not do/while
exports.specialForms["do"] = function(args, env) {
  var value = false;
  args.forEach( function(arg) {
    value = evaluate.evalSyntax(arg, env);
  });

  return value;
};

exports.specialForms["def"] = function(args, env) {
  if ( args.length != 2 || args[0].type != "word" ) {
    throw new SyntaxError("*** Incorrect `def` statement");
  }

  var value = evaluate.evalSyntax( args[1], env );
  env[ args[0].name ] = value;

  return value;
};

exports.specialForms["fn"] = function(args, env) {
  if (!args.length) {
    throw new SyntaxError("*** Expected function body");
  }

  function name(expr) {
    if (expr.type != "word") {
      throw new SyntaxError("*** Unexpected parameter type");
    }

    return expr.name;
  }

  var argNames = args.slice(0, args.length - 1).map(name);
  var body = args[args.length - 1];

  return function() {
    if (arguments.length != argNames.length) {
      throw new TypeError("*** Incorrect number of arguments");
    }

    var localEnv = Object.create(env);
    for (var i = 0; i < arguments.length; i++) {
      localEnv[ argNames[i] ] = arguments[i];
    }

    return evaluate.evalSyntax(body, localEnv);
  }
}

// Environment: variable identifiers corresponding to their values.
//              This includes language constants, which are defined
//              below.
var topEnv = Object.create(null);

topEnv["true"] = true;
topEnv["false"] = false;

["+", "-", "*", "/", "==", "<", ">"].forEach( function(op) {
  topEnv[op] = new Function("a, b", "return a " + op + " b;");
});

topEnv["write"] = function(value) {
  console.log(value);

  return value;
};

function run() {
  var env = Object.create(topEnv);

  var program = Array.prototype.slice
    .call(arguments, 0)
    .join("\n")

  return evaluate.evalSyntax( parser.parse(program), env );
}

// Read source files to run
fs.readFile( process.argv[2], function(err, data) {
  if (err) {
    throw err;
  }

  var program = data.toString().split("\n").join("");
  run( program );
});

