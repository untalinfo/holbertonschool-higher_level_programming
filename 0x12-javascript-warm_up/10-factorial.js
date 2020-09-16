#!/usr/bin/node
// script that computes and prints a factorial

const argument = parseInt(process.argv[2]);

function factorial (n) {
  if (n > 1) {
    return n * factorial(n - 1);
  }
  return 1;
}

if (Number.isNaN(argument) || argument === 0 || argument === 1) {
  console.log(1);
} else {
  console.log(factorial(argument));
}
