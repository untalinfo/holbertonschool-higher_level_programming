#!/usr/bin/node
const argument = parseInt(process.argv[2]);
let i = 0;
const square = 'X';
if (!(Number.isInteger(argument)) || !(argument)) {
  console.log('Missing size');
}
while (i < argument) {
  console.log(square.repeat(argument));
  i++;
}
