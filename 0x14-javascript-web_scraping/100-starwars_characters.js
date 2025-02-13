#!/usr/bin/node
/* This script prints all characters of a Star Wars movie */

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the command-line argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // Construct API URL

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters; // List of character URLs

  // Fetch and print each character's name
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
