#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = 'X';
    for (let i = 1; i < this.width; i++) {
      str += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }
}

module.exports = Rectangle;
