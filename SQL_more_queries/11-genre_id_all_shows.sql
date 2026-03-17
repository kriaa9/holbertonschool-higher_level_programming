-- Lists all shows from hbtn_0d_tvshows with their genre IDs
-- Uses LEFT JOIN to include shows even if they have no genre linked
-- LEFT JOIN keeps all rows from tv_shows and shows NULL for genre_id
-- when there is no matching record in tv_show_genres
-- Displays: tv_shows.title and tv_show_genres.genre_id (NULL if no genre)
-- Results sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
