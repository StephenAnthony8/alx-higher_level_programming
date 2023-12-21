#!/usr/bin/node

const num = parseInt(process.argv[2]);
let numStr = '';
if (isNaN(num) === false) {
  /* numStr = 'X'; */
  for (let j = 1; j <= num; j++) {
    numStr = numStr + 'X';
  }

  for (let i = 1; i <= num; i++) {
    console.log(numStr);
  }
} else { console.log('Missing size'); }
