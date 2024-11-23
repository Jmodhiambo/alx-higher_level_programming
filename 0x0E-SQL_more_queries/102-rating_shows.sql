-- Script to list all TV shows and their rating sum from the database hbtn_0d_tvshows_rate
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating sum

SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS ts
       INNER JOIN `tv_show_ratings` AS r
       ON ts.`id` = r.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC;
