-- List all the cities in the database
-- Display :cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
SELECT c.id, c.name, s.name
FROM states AS s
JOIN cities AS c
ON c.state_id = s.id
ORDER BY c.id ASC;
