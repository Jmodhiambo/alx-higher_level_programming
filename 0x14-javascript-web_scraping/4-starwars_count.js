#!/usr/bin/node

/* This script prints the number of movies where the character “Wedge Antilles” is present. */

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  const movies = data.results;
  let count = 0;

  movies.forEach(movie => {
    movie.characters.forEach(characterUrl => {
      if (characterUrl.includes('/18/')) { // Matching character ID 18
        count++;
      }
    });
  });

  console.log(count);
});
