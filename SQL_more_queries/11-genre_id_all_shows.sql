-- Task: List all shows with linked genre IDs or NULL if no genre
-- File: 11-genre_id_all_shows.sql

-- Select shows and their linked genre IDs or NULL if no genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
