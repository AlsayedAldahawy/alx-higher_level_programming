#!/usr/bin/node

function fact (x) {
  if (x < 0) {
    return (-1);
  }

  if (isNaN(x) || x === 1) {
    return 1;
  }

  return x * fact(x - 1);
}

console.log(fact(+process.argv[2]));
