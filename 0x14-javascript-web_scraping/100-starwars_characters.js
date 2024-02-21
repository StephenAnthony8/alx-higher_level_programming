#!/usr/bin/node

const request = require('request');

const urlName = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const otherUrl = 'https://swapi-api.alx-tools.com/api/people';

let nameList = []
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
          /* nameList.push */console.log(name.name);
        }
      });
    }
  }
});

/* request({ url: otherUrl, json: true }, (error, response, body) => {
  if (error || (String(response.statusCode) !== '200')) {
    console.error((error) || response.statusCode);
  } else {
    for (people of body.results) {
      if (nameList.includes(people.name)) {
        console.log(people.name);
      }
    }
  }
}) */