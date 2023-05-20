-- -- listall shows without the genre comedy in the database
SELECT DISTINCT title
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
LEFT JOIN tv_genres AS tg 
ON tg.id = tsg.genre_id
WHERE title NOT IN (
	SELECT title
	FROM tv_shows AS ts 
	JOIN tv_show_genres AS tsg 
	ON ts.id = tsg.show_id
	JOIN tv_genres AS tg
	ON tg.id = tsg.genre_id 
	WHERE tg.name =  'Comedy') 
ORDER BY title;
