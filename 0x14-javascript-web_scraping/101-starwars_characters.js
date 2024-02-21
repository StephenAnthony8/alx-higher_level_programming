#!/usr/bin/node

const request = require('request');

const urlName = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request({ url: urlName, json: true }, (error, response, body) => {
  if (error || (String(response.statusCode) !== '200')) {
    console.error((error) || response.statusCode);
  } else {
    for (const character of body.characters) {
      /* console.log(character); */
      request({ url: character, json: true }, (error, response, name) => {
        if (error || (String(response.statusCode) !== '200')) {
          console.error((error) || response.statusCode);
        } else {
          console.log(name.name);
        }
      });
    }
  }
});
