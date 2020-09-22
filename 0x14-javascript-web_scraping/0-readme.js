#!/usr/bin/node
// script that reads and prints the content of a file.

const file = require('fs');
file.readFile(process.argv[2], function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data.toString('utf8'));
});
