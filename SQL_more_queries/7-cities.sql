-- Creates the database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Creates the cities table if it doesn't already exist
-- id: unique, auto-incremented integer serving as the primary key
-- state_id: integer that cannot be null, references the id column in the states table
-- name: string up to 256 characters, cannot be null
-- The FOREIGN KEY constraint ensures that state_id must match an existing id in the states table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
