#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const reverse = [];
  for (const x in list) {
    reverse.unshift(list[x]);
  }
  return (reverse);
};
