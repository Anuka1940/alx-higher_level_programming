#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: node concatFiles.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

try {
  const content1 = fs.readFileSync(sourceFile1, 'utf-8');
  const content2 = fs.readFileSync(sourceFile2, 'utf-8');

  const concatenatedContent = content1 + content2;

  fs.writeFileSync(destinationFile, concatenatedContent);
  console.log('Files concatenated successfully.');
} catch (error) {
  console.error('An error occurred:', error.message);
}
