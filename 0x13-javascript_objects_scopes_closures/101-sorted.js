#!/usr/bin/node
const dict = require('./101-data').dict;

const dict2 = {};

for (const key in dict) {
  if (dict[key] in dict2) {
    dict2[dict[key]].push(key);
  } else {
    dict2[dict[key]] = [key];
  }
}

console.log(dict2);
