#!/usr/bin/node
// script that display the status code of a GET request
const URL = process.argv[2];
const request = require('request');

request(URL, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
