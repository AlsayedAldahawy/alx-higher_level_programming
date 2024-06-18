#!/usr/bin/node

function fact (N) {
  if (N < 0) {
    return -1;
  }
  if (isNaN(N) || N === 1 || N === 0) {
    return (1);
  }

  return (N * fact(N - 1));
}

console.log(fact(+process.argv[2]));
