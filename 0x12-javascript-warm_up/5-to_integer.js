#!/usr/bin/node
const parameter = parseInt(process.argv[2]);
if (!(parameter)) {
  console.log('Not a number');
} else if (Number.isInteger(parameter)) {
  console.log('Number: ' + parameter);
} else {
  console.log('Not a number');
}
