-- Lists all shows that have at least one genre linked from hbtn_0d_tvshows
-- Uses INNER JOIN between tv_shows and tv_show_genres tables
-- INNER JOIN ensures only shows with at least one genre are included
-- Displays: tv_shows.title and tv_show_genres.genre_id
-- Results sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
