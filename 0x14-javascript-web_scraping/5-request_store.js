#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const URL = process.argv[2];
const fs = require('fs');
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', function (err, data) {
    if (err) {
      console.log(err);
    }
  });
});
