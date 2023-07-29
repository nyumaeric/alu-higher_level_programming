-- Script to create a table called "second_table" in the current database in your MySQL server and add multipul rows.
-- Querry to create a table called "second_table" in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table (id INT,
name VARCHAR(256),
score INT
);
-- Querry to add in values
INSERT INTO second_table (id, name, score)
Values (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
