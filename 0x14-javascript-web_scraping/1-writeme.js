#!/usr/bin/node

const fs = require('fs');

fs.open(process.argv[2], 'w', (err, fd) => {
  if (err) {
    console.error(err);
  } else {
    fs.write(fd, process.argv[3], (err, bytes) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
