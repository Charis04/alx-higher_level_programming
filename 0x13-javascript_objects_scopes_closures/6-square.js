#!/usr/bin/node

const Square = require('./5-square');

class Square extends Square {
  charPrint (c = 'X') {
    str = c;
    for (let i = 1; i < this.width; i++) {
      str += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }
}

module.exports = Square;
