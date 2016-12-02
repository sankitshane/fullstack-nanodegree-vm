-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Load the file in vagrant psql ny \i tournament.sql

-- Create a database tournament
CREATE DATABASE tournament;

-- connect to the database tournament by \c tournament
\c tournament;

--Create table players
CREATE TABLE players (
      Id SERIAL PRIMARY KEY NOT NULL,
      Name VARCHAR(20) NOT NULL
);

-- Create table results
CREATE TABLE results (
      Id INT references players(Id),
      Wins INT,
      Matches INT
);

--Create table rounds
CREATE TABLE rounds (
      Player1 INT NOT NULL,
      Player2 INT NOT NULL,
      Winner INT NOT NULL,
      Loser INT NOT NULL
);
