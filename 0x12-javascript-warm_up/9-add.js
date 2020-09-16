#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (num1 && num2) {
  console.log(num1 + num2);
} else {
  console.log('NaN');
}
