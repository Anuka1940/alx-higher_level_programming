-- display all records of the second_table
SELECT score, name FROM second_table WHERE name is not null and name != '' ORDER BY score DESC;
