-- Lists all shows and their linked genres from hbtn_0d_tvshows database
-- Uses LEFT JOIN to include shows even if they have no genre linked
-- First LEFT JOIN connects tv_shows to tv_show_genres (junction table)
-- Second LEFT JOIN connects tv_show_genres to tv_genres (genre names)
-- Shows without a genre will display NULL in the genre name column
-- Displays: tv_shows.title and tv_genres.name
-- Results sorted by tv_shows.title and tv_genres.name in ascending order
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
