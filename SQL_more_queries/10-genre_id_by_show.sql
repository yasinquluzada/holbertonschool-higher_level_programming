-- Task 10: List all shows that have at least one genre linked, with their genre IDs.

-- Displays: tv_shows.title - tv_show_genres.genre_id (only shows with linked genres)
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
