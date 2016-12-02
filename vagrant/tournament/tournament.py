#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM rounds")
    c.execute("UPDATE results set Matches = 0,Wins = 0")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM results")
    c.execute("DELETE FROM players")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    count = c.fetchone()
    conn.close()
    res = int(count[0])
    return res

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO players (Name) VALUES (%s)" ,(name,))
    c.execute("INSERT INTO results (Id,Wins,Matches) VALUES ((SELECT Id FROM players WHERE Name = %s),%s,%s)",(name,int(0),int(0),))
    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT players.ID, players.Name, results.Wins , results.Matches FROM players JOIN results ON players.Id = results.Id ")
    play = [(str(row[0]),str(row[1]),int(row[2]),int(row[3])) for row in c.fetchall()]
    conn.close()
    return play

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE rounds SET Winner = %s ,Loser = %s WHERE Player1 = %s and Player2 = %s or Player1 = %s and Player2 = %s",( winner,loser,winner,loser,loser,winner,))
    c.execute("UPDATE results SET Wins = Wins + 1 , Matches = Matches + 1 WHERE Id = %s",(winner,))
    c.execute("UPDATE results SET Matches = Matches + 1 WHERE Id = %s",(loser,))
    conn.commit()
    conn.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    c= conn.cursor()
    c.execute("SELECT players.Id, players.Name, results.Wins FROM players JOIN results ON players.Id = results.Id ORDER BY results.Wins DESC")
    player = c.fetchall()
    conn.close()
    res = []
    for i in xrange(0,len(player),2):
        res.append((int(player[i][0]),player[i][1],int(player[i+1][0]),player[i+1][1]))

    return res
