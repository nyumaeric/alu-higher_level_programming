-- Script that creates the table unique_id in database provided.
-- Query that creates the table unique_id in database provided.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);

