#!/usr/bin/node
/* This script prints all characters of a Star Wars movie in order */

const request = require('request');

const movieId = process.argv[2]; // Get movie ID from command-line argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters; /* Array of character URLs */

  /* Function to request each character sequentially */
  function fetchCharacter (index) {
    if (index >= characters.length) return; /* Stop when all characters are fetched */

    request(characters[index], (err, response, body) => {
      if (!err) {
        console.log(JSON.parse(body).name);
      }
      fetchCharacter(index + 1); /* Recursive call to fetch the next character */
    });
  }

  fetchCharacter(0); // Start fetching from the first character
});
