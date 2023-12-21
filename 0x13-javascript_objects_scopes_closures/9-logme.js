#!/usr/bin/node

function countFunct () {
  if (!countFunct.counter && countFunct.counter !== 0) {
    countFunct.counter = -1;
  }
  countFunct.counter++;
  return (countFunct.counter);
}
exports.logMe = function (item) {
  console.log(`${countFunct()}: ${item}`);
};
