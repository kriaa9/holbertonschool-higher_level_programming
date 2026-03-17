-- Lists all shows from hbtn_0d_tvshows that have no genre linked
-- Uses LEFT JOIN to get all shows, then filters with WHERE clause
-- WHERE tv_show_genres.genre_id IS NULL keeps only shows with no matching genre
-- This works because LEFT JOIN returns NULL for non-matching right table rows
-- Displays: tv_shows.title and tv_show_genres.genre_id (always NULL)
-- Results sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
