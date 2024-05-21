#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

req(url, (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(path, body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
