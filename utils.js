// Name:        utils.js
// Author:      Josh Hartigan
// Description: Utilities for the Minim language

exports.cutWhitespace = function(string) {
  var first = string.search(/\S/);
  if (first == -1) {
    return "";
  }

  return string.slice(first);
}

