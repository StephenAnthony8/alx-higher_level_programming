#!/usr/bin/node

const request = require('request');

const swUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request({ url: swUrl, json: true }, (error, response, body) => {
  if (error || (String(response.statusCode) !== '200')) {
    console.error((error) || response.statusCode);
  } else {
    console.log(body.title);
  }
});
