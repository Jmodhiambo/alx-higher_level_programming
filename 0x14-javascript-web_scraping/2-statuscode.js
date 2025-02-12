#!/usr/bin/node
/* Gets the status code of the GET request. */

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (response) {
    console.log('code:', response.statusCode);
  }
});
