#!/usr/bin/node
const fs = require('fs');

const filename = process.argv[2];
fs.readFile(filename, 'utf8', (error, file) => {
  if (error) {
    console.log(error);
  } else {
    console.log(file);
  }
});
