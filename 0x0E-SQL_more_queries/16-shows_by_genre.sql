-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT ts.title AS title, tg.name AS name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres
ON ts.id = tv_show_genres.show_id
LEFT JOIN tv_genres AS tg
ON tg.id = tv_show_genres.genre_id
ORDER BY title, name
