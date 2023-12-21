#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  /* constructor (size) {
    // Call the constructor of the parent class
    super(size);
  } */

  charPrint (c) {
    c = (c === undefined ? 'X' : c);
    for (let i = 0; i < this.height; i++) {
      let xSize = '';
      for (let j = 0; j < this.width; j++) {
        xSize += c;
      }
      console.log(xSize);
    }
  }
}

module.exports = Square;
