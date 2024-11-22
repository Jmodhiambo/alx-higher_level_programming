-- Script to list all Comedy shows from the database hbtn_0d_tvshows
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by show title
-- The tv_genres table contains only one record where name = 'Comedy' (id can be different)

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
