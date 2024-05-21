#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let total = 0;
request(url, (error, response, body) => {
  if (error) console.log(error);
  body = JSON.parse(body).results;
  let i = 0;
  for (i; i < body.length; i++) {
    const character = body[i].characters;
    for (let count = 0; count < character.length; count++) {
      const id = character[count].split('/')[5];
      if (id === '18') {
        total += 1;
      }
    }
  }
  console.log(total);
});
