#!/usr/bin/node
/* Gets the status code of the GET request. */

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
