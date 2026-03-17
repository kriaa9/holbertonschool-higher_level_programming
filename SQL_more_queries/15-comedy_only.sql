-- Lists all Comedy shows from hbtn_0d_tvshows database
-- Joins three tables: tv_shows -> tv_show_genres -> tv_genres
-- tv_show_genres is the junction table linking shows to genres
-- Filters results to only shows where the genre name is "Comedy"
-- Displays only the show title (tv_shows.title)
-- Results sorted by show title in ascending order (alphabetical)
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
