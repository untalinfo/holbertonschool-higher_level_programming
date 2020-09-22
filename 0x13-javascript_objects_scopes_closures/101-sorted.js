#!/usr/bin/node
// script that imports a dictionary of occurrences by user id and computes
// a dictionary of user ids by occurrence
const { dict } = require('./101-data');
const newDict = {};
for (const k in dict) {
  if (dict[k] in newDict) {
    newDict[dict[k]].push(k);
  } else {
    newDict[dict[k]] = [k];
  }
}
console.log(newDict);
