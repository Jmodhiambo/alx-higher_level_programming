#!/usr/bin/node

/* This script prints the number of movies where the character “Wedge Antilles” (ID 18) is present. */

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const data = JSON.parse(body);
      const movies = data.results;
      const count = movies.filter(movie =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      ).length;

      console.log(count);
    } catch (parseError) {
      console.error('Failed to parse JSON:', parseError.message);
    }
  }
});
