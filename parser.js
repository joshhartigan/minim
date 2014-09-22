// Name:        parser.js
// Author:      Josh Hartigan
// Description: Parse Minim source code into an AST

var utils = require("./utils");

var parseExpression = function(program) {
  program = utils.cutWhitespace(program);

  var match, expr;

  if ( match = /^"([^"]*)"/.exec(program) ) {
    expr = { type: "value", value: match[1] };
  } else if ( match = /^\d+\b/.exec(program) ) {
    expr = { type: "value", value: Number( match[0] ) };
  } else if ( match = /^[^\s(),"]+/.exec(program) ) {
    expr = { type: "word", name: match[0] };
  } else {
    throw new SyntaxError("*** Unexpected syntax:" + program);
  }

  return parseApply( expr, program.slice( match[0].length ) );
};

var parseApply = function(expr, program) {
  program = utils.cutWhitespace(program);

  if (program[0] != "(") {
    return { expr: expr, rest: program };
  }

  program = utils.cutWhitespace( program.slice(1) );
  expr = { type: "apply", operator: expr, args: [] };
  while ( program[0] != ")" ) {
    var arg = parseExpression(program);
    expr.args.push(arg.expr);
    program = utils.cutWhitespace(arg.rest);

    if ( program[0] == "," ) {
      program = utils.cutWhitespace(program.slice(1));
    } else if ( program[0] != ")" ) {
      throw new SyntaxError("*** Expected ',' or ')'");
    }
  }

  return parseApply( expr, program.slice(1) );
};

exports.parse = function(program) {
  var result = parseExpression(program);
  if ( utils.cutWhitespace(result.rest).length > 0 ) {
    throw new SyntaxError("*** Unexpected text after program");
  }

  return result.expr;
};

