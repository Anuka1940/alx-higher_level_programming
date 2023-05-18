-- create and insert in a table
CREATE TABLE if not EXISTS second_table (
	id INTEGER,
	name VARCHAR(256),
	score INTEGER
);
INSERT INTO second_table (id, name, score) VALUES(1, "john", 10);
INSERT INTO second_table (id, name, score) VALUES(2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES(3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES(4, "George", 8);
