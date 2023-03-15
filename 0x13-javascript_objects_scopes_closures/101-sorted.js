#!/usr/bin/node

const dict = require('./101-data').dict;
const newdict = {};
for (const each in dict) {
  const occurence = dict[each];
  if (!(occurence in newdict)) {
    newdict[occurence] = [];
  }
  newdict[occurence].push(each);
}
console.log(newdict);
