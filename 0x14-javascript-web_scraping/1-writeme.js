#!/usr/bin/node
/* This script writes a string to a file. */

const fs = require('fs');

/* Get the file path and content from the command line arguments */
const filePath = process.argv[2];
const content = process.argv[3];

/* Write the content to the file in utf-8 encoding */
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
