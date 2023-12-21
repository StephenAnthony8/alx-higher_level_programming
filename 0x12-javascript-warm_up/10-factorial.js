#!/usr/bin/node

function recurVal (val) {
  if (isNaN(val) === true || val < 1) {
    val = 1;
  } else {
    val *= recurVal(val - 1);
  }
  return (val);
}

console.log(recurVal(process.argv[2]));
