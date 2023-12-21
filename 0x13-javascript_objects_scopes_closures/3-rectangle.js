#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w && h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let xStr = '';
      for (let j = 0; j < this.width; j++) {
        xStr += 'X';
      }
      console.log(xStr);
    }
  }
}

module.exports = Rectangle;
