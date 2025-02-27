-- Script to list all shows and their linked genres from the database hbtn_0d_tvshows
-- Each record displays: tv_shows.title - tv_genres.name
-- If a show doesn't have a genre, NULL will be displayed in the genre column
-- Results are sorted by the show title and genre name in ascending order

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
