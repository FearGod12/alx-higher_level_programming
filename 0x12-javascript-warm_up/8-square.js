#!/usr/bin/node

const arg = process.argv[2] * 1;
if (!isNaN(arg)) {
  const string = 'X';
  for (let i = 0; i < arg; i++) {
    console.log(string.repeat(arg));
  }
} else {
  console.log('Missing size');
}
