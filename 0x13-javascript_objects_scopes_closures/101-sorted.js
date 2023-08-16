#!/usr/bin/node

const { dict } = require('./101-data.js');

const reversedDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!(occurrences in reversedDict)) {
    reversedDict[occurrences] = [];
  }
  reversedDict[occurrences].push(userId);
}

console.log(reversedDict);
