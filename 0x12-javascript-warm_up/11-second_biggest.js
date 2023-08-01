#!/usr/bin/node

function secondBiggest (num) {
  const sortedNum = num.sort((a, b) => b - a);
  return sortedNum[1] || 0;
}

const args = process.argv.slice(2).map(Number);
console.log(secondBiggest(args));
