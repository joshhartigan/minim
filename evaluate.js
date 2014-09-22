// Name:        evaluate.js
// Author:      Josh Hartigan
// Description: Evaluate Minim ASTs

var minim = require("./minim");

exports.evalSyntax = function(expr, env) {
  switch(expr.type) {
  case "value":
    return expr.value;

  case "word":
    if (expr.name in env) {
      return env[expr.name];
    } else {
      throw new ReferenceError("Undefined identifier: " + expr.name);
    }

  case "apply":
    if (expr.operator.type == "word" &&
      expr.operator.name in minim.specialForms) {
      return minim.specialForms[expr.operator.name](expr.args, env);
    }

    var op = exports.evalSyntax(expr.operator, env);
    if (typeof op != "function") {
      throw new TypeError("*** Applying a non-function");
    }

    return op.apply(null, expr.args.map(function(arg) {
      return exports.evalSyntax(arg, env);
    }));
  }
}

