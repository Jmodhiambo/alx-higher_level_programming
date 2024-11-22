-- This script that creates the database hbtn_0d_usa and the table cities.
-- cities id is unique, auto generated, can’t be null and is a primary key.
-- cities state_id id integer, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- cites name can't be null.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states(id)
) ENGINE=InnoDB;
