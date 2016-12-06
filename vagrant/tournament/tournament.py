import psycopg2


def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("We probably missed a packet, Connection error.")


def deleteMatches():
    """Remove all the match records from the database."""
    conn, c = connect()
    c.execute("TRUNCATE matches ")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn, c = connect()
    c.execute("TRUNCATE players CASCADE")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn, c = connect()
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

    conn, c = connect()
    c.execute("INSERT INTO players (Name) VALUES (%s)", (name, ))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,\
    or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, c = connect()
    select_q = """SELECT players.id,players.name,(SELECT count(winner)
                  FROM matches WHERE winner = players.id) AS wins,
                  (SELECT count(*) FROM matches
                  WHERE winner = players.id OR loser = players.id)
                  AS match FROM players"""
    c.execute(select_q)
    play = [(str(row[0]),
            str(row[1]),
            int(row[2]),
            int(row[3])) for row in c.fetchall()]
    conn.close()
    return play


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, c = connect()
    insert_q = "INSERT INTO matches(winner,loser) VALUES (%s,%s) "
    c.execute(insert_q, (winner, loser))
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
    player = playerStandings()
    player.sort(key=lambda tup: tup[2])
    res = []
    for i in xrange(0, len(player), 2):
        res.append((int(player[i][0]),
                    player[i][1],
                    int(player[i+1][0]),
                    player[i+1][1]))

    return res
