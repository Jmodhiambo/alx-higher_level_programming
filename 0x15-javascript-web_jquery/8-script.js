/* This fetches and lists the title for all movies from an API */

$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (film) {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
});
