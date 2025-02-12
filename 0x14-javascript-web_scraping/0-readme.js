#!/usr/bin/node
/* This script reads and prints the content of a file using the request module. */

const fs = require('fs');

const filePath = process.argv[2];

// Read the file content
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
