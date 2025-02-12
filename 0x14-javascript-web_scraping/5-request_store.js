#!/usr/bin/node
/* This script gets the content of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const fileName = process.argv[3];

request({ url: apiUrl, encoding: 'utf-8' }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileName, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
