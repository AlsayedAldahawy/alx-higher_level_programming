-- Creates the database hbtn_0d_usa with the table cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    FOREIGN KEY (state_id) REFERENCES states.state_id,
    name VARCHAR(256) NOT NULL,
);
