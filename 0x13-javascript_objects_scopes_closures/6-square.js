#!/usr/bin/node
// class Square that defines a square and inherits from Square of
// 5-square.js
// * You must use the class notation for defining your class and extends
// * Create an instance method called charPrint(c) that prints the
// rectangle using the character c
// * If c is undefined, use the character X

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c = 'X') {
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
};
