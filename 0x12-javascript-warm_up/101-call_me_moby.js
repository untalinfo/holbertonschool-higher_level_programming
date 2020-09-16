#!/usr/bin/node
// function that executes x times a function.
let i = 0;
exports.callMeMoby = function (x, theFunction) {
  while (i < x) {
    theFunction();
    i += 1;
  }
};
