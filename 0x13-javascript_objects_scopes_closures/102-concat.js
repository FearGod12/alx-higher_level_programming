#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
fs.readFile(args[2], (err1, data1) => {
  if (err1) throw err1;
  fs.readFile(args[3], (err2, data2) => {
    if (err2) throw err2;
    const readString = data1 + data2;
    fs.writeFile(args[4], readString, (err3) => {
      if (err3) throw err3;
    });
  });
});
