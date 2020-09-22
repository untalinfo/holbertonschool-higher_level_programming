#!/usr/bin/node
// class Rectangle that defines a rectangle:
// * You must use the class notation for defining your class
// * The constructor must take 2 arguments w and h
// * Initialize the instance attribute width with the value of w
// * Initialize the instance attribute height with the value of h
// * Create an instance method called print() that prints the
// rectangle using the character X

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rot = this.width;
    this.width = this.height;
    this.height = rot;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
