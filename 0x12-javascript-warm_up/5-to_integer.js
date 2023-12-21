#!/usr/bin/node

const arg3 = process.argv[2];
if (arg3 !== undefined && (isNaN(parseInt(arg3)) === false)) {
  console.log('My number: ' + arg3);
} else { console.log('Not a number'); }
