-- list all genres in the database by their ratings
SELECT name, SUM(rate) AS rating
FROM tv_shows AS ts
JOIN tv_show_ratings tsr
ON ts.id = tsr.show_id
JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
JOIN tv_genres AS tg
ON tg.id = tsg.genre_id
GROUP BY name
ORDER BY rating DESC;
