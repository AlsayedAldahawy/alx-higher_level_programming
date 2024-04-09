#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const args2 = args.sort(function (a, b) {
  return b - a;
});
console.log(args2[1] ?? 0);
