#!/usr/bin/node

let n = 0;
exports.logMe = function (item) {
  n++;
  console.log(n + ': ' + item);
};
