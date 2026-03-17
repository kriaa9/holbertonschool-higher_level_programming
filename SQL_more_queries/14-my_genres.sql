-- Lists all genres of the show "Dexter" from hbtn_0d_tvshows database
-- Joins three tables: tv_genres -> tv_show_genres -> tv_shows
-- tv_show_genres links shows to their genres via show_id and genre_id
-- Filters results to only the show titled "Dexter" using WHERE clause
-- Displays only the genre name (tv_genres.name)
-- Results sorted by genre name in ascending order (alphabetical)
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
