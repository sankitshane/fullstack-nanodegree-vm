-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Load the file in vagrant psql ny \i tournament.sql

-- Create a database tournament
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- connect to the database tournament by \c tournament
\c tournament;

--Create table players
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name TEXT
);

--Create table matches
CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    winner INTEGER REFERENCES players(id),
    loser INTEGER REFERENCES players(id)
);
