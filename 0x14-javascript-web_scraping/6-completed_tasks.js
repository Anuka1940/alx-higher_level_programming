#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, (error, response, body) => {
  if (error) console.log(error);
  body = JSON.parse(body);
  const completedTask = {};
  for (let i = 0; i < body.length; i++) {
    const userId = body[i].userId;
    if (body[i].completed && !completedTask[userId]) {
      completedTask[userId] = 0;
    }
    if (body[i].completed) {
      completedTask[userId] += 1;
    }
  }
  console.log(completedTask);
});
