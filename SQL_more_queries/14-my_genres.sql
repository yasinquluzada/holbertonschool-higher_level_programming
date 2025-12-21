-- Task 14: List all genres of the show Dexter.
-- Display: tv_genres.name (sorted ASC)

SELECT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS sg ON g.id = sg.genre_id
JOIN tv_shows AS s ON s.id = sg.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
