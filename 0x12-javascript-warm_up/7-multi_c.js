#!/usr/bin/node

const arg = process.argv[2] * 1;
if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
