#!/usr/bin/node

const request = require('request');

const urlName = process.argv[2] + '?completed=true';

request({ url: urlName, json: true }, (error, response, body) => {
  if (error || (String(response.statusCode) !== '200')) {
    console.error((error) || response.statusCode);
  } else {
    const rtnObj = {};
    for (const item of body) {
      if (rtnObj[item.userId] === undefined) {
        rtnObj[item.userId] = 1;
      } else {
        rtnObj[item.userId] = rtnObj[item.userId] + 1;
      }
    }
    console.log(rtnObj);
  }
});
