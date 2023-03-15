#!/usr/bin/node

exports.logMe = function (item) {
  let n = 0;
  return function (item) {
    n++;
    console.log(n + ': ' + item);
  };
}();
