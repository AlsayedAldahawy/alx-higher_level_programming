#!/usr/bin/node

const list = require('./100-data.js').list;
const list2 = list.map((x, i) => x * i);
// the index i is automatically incremented by the map itself for each iteration over the array.
console.log(`${list}\n${list2}`);
