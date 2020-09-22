#!/usr/bin/node
// computes the number of tasks completed by user id

const URL = process.argv[2];
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  const numTask = {};
  for (const x in json) {
    const data = json[x];
    if (data.completed === true) {
      const id = data.userId;
      if (id in numTask) {
        numTask[id] += 1;
      } else {
        numTask[id] = 1;
      }
    }
  }
  console.log(numTask);
});
