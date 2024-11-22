-- This scipt creates table force_name on MySQL server
-- Database name is passed an argument of the mysql command
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
