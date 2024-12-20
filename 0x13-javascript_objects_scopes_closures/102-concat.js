#!/usr/bin/node

const fs = require('fs');

// Get the file paths from the command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const destination = process.argv[4];

try {
  // Read the contents of the first and second files
  const contentA = fs.readFileSync(fileA, 'utf-8');
  const contentB = fs.readFileSync(fileB, 'utf-8');

  // Concatenate and write the contents to the destination file
  fs.writeFileSync(destination, contentA + contentB, 'utf-8');
} catch (err) {
  console.error(err.message);
}
