#!/usr/bin/node
//  reads and prints the content of a file.

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    const errorMessage = {
      Error: err.message,
      errno: err.errno,
      code: err.code,
      syscall: err.syscall,
      path: err.path
    };
    console.error(errorMessage);
  } else {
    console.log(data);
  }
});
