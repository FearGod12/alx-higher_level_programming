#!/usr/bin/node

const arg = process.argv[2] * 1;
if (!isNaN(arg)) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
