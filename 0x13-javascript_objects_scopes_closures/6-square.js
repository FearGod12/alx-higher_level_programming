#!/usr/bin/node

const SquareClass = require("./5-square");

class Square extends SquareClass {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let character;
    if (c) {
      character = c;
    } else {
      character = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
