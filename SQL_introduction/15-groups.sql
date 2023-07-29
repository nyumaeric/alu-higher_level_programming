-- Script to list the number of records with the same score in the table "second_table" of the database provided.
-- Querry to list the number of records with the same score in the table "second_table" of the database provided.
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score DESC;
