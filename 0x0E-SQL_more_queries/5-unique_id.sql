-- This script that creates the table unique_id with id having a default of 1
-- the id needs to be unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
