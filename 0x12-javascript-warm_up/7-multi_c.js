#!/usr/bin/node
const argument = parseInt(process.argv[2]);
let i = 1;
if (!(Number.isInteger(argument))) {
  console.log('Missing number of occurrences');
}
while (i <= argument) {
  console.log('C is fun');
  i++;
}
