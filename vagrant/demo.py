import psycopg2

conn = psycopg2.connect("dbname=vagrant")
c = conn.cursor()
c.execute("SELECT * FROM demo")
post = c.fetchall()
conn.close()

print post
