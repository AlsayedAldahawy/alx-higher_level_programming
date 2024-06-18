#!/usr/bin/node

if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
