#!/usr/bin/node

const req = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  console.log(body.title);
});
