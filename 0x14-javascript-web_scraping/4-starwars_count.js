#!/usr/bin/node

const request = require('request');

const swUrl = process.argv[2];

const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';

let count = 0;
request({ url: swUrl, json: true }, (error, response, body) => {
  if (error || (String(response.statusCode) !== '200')) {
    console.error((error) || response.statusCode);
  } else {
    for (const x of body.results) {
      if (x.characters.includes(wedge)) {
        count++;
      }
    }
    console.log(count);
  }
});
