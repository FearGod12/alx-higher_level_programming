#!/usr/bin/node

const args = process.argv;
let array;
if (args.lenght < 4) {
  console.log(0);
} else {
  array = args.slice(2).sort((a, b) => b - a);
  console.log(array[1]);
}
