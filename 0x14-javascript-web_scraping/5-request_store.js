#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const urlName = process.argv[2];

request({ url: urlName }, (error, response, body) => {
  if (error || (String(response.statusCode) !== '200')) {
    console.error((error) || response.statusCode);
  } else {
    fs.open(process.argv[3], 'w', (err, fd) => {
      if (err) {
        console.error(err);
      } else {
        fs.write(fd, String(body), (err, bytes) => {
          if (err) {
            console.error(err);
          }
        });
      }
    });
  }
});
