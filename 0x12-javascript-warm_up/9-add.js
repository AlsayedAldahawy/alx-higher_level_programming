#!/usr/bin/node

function add (a, b) {
  return Number(a) + Number(b);
}

if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(NaN);
} else {
  console.log(add(process.argv[2], process.argv[3]));
}
