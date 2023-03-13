#!/usr/bin/node

function add (a, b) {
  const arg1 = process.argv[2] * 1;
  const arg2 = process.argv[3] * 1;
  console.log(arg1 + arg2);
}

add();
