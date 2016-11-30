-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE DATABASE tournament;

CREATE TABLE players (
      Id SERIAL PRIMARY KEY NOT NULL,
      Name VARCHAR(20) NOT NULL
);

CREATE TABLE results (
      Id INT references players(Id),
      Wins INT,
      Matches INT
);

CREATE TABLE rounds (
      Player1 INT NOT NULL,
      Player2 INT NOT NULL,
      Winner INT NOT NULL,
      Loser INT NOT NULL
);
