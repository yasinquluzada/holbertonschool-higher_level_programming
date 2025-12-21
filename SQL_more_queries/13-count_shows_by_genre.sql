-- Task 13: List all genres and the number of shows linked to each (only genres with at least one show).
SELECT
  tg.name AS genre,
  COUNT(*) AS number_of_shows
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg
  ON tg.id = tsg.genre_id
GROUP BY tg.id, tg.name
ORDER BY number_of_shows DESC;
