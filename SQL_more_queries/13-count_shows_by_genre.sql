-- Lists all genres and the number of shows linked to each from hbtn_0d_tvshows
-- Joins three tables: tv_genres, tv_show_genres, and tv_shows
-- tv_show_genres acts as a linking/junction table between shows and genres
-- COUNT counts the number of shows associated with each genre
-- GROUP BY groups results by genre name to aggregate the count
-- HAVING filters out genres with no linked shows (same effect as INNER JOIN here)
-- Results sorted by number_of_shows in descending order (most popular genres first)
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
