-- Creates the database hbtn_0d_usa with table states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE AUTO NOT NULL,
    name VARCHAR(256) NOT NULL
);
