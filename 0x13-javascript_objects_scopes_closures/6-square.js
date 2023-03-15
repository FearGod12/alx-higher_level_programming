#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((Number.isInteger(w) && w > 0) && (Number.isInteger(h) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const c = this.width;
    this.width = this.height;
    this.height = c;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
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
