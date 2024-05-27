#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/film/' + id;

req(url, (error, response, body) => {
  if (error) console.log(error);
  body = JSON.parse(body);
});
