#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

req(url, (error, response, body) => {
  if (error) console.log(error);
  body = JSON.parse(body);
  const characters = body.characters;
  for (let i = 0; i < characters.length; i++) {
    req(characters[i], (error, response, body) => {
      if (error) console.log(error);
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
