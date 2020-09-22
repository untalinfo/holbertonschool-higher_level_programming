#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.

const URL = process.argv[2];
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (const x in results) {
    const characters = results[x].characters;
    for (const y in characters) {
      if (characters[y].includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
