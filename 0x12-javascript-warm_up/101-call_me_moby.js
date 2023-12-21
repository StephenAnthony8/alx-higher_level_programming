#!/usr/bin/node
const callMeMoby = function (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
};

module.exports = { callMeMoby };
