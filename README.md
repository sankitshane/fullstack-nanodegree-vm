rdb-fullstack
=============

## Description:

It is a application that uses backend database to execute a Swiss tournament matchup

### Software Used:
* vagrant
* Virtual Box 4.12.0

### Setup

1. Fort the directory.
2. Clone the directory to your system.
3. Install the above Software
4. On Git Bash go to the directory and then to vagrant directory
5. Execute vagrant up
6. Execute vagrant ssh
7. Go to the root directory "cd vagrant/tournament"
8. Execute psql to go to PostgreSQL terminal.
  PostgreSQL is already installed in the Virtual Machine.
9. $ /i tournament to create the tournament database, connect to it and create the tables.
10. ctrl - Z to get back to the terminal.
11. Execute tournament_test.py to run the code and check all functions
are working correctly.
$ python tournament_test.py
