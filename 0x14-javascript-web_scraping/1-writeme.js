#!/usr/bin/node

const fs = require('fs');

// Get the file path and the string to write from the command line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
    console.error('Please provide both a file path and a string to write.');
    process.exit(1);
}

// Write the content to the file in utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
    if (err) {
        console.error(err);
    } else {
        console.log('Content written successfully');
    }
});

