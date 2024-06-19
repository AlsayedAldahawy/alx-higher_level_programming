#!/usr/bin/node

const args = process.argv.slice(2);
const argsSorted = args.sort(function (a, b) { return b - a; });
console.log(argsSorted[1] ?? 0);
