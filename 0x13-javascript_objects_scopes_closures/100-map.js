#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
// the index i is automatically incremented by the map itself for each iteration over the array.
