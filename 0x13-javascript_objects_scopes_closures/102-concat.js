#!/usr/bin/node

const fs = require('fs');

try {
  const content = fs.readFileSync(process.argv[2]).toString() + fs.readFileSync(process.argv[3]).toString();

  fs.writeFileSync(process.argv[4], content);
} catch (error) {}
