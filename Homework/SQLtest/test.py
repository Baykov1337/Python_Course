import sqlite3 #import SQL Lite3 module

conn = sqlite3.connect('test.sqlite') #connect to the database - if the fies does not exists this will create empty db

cur = conn.cursor() #this would allow us to execute commands in SQLIte

cur.execute("""create table test_table (id integer , name text)""")  # this will create table into our database - 

conn.commit()
# cur.execute("insert into test_table values (1,'Boyan')")
# cur.execute("insert into test_table values (2,'Ivan')")
# cur.execute("insert into test_table values (3,'Petar')")
#this way you can execute 3 different statements for insert 3 different rows

#another approach to insert multiple values into a table is this 
cur.execute("insert into test_table values (1,'Boyan'), (2,'Ivan'), (3,'Petar')")

#cur.execute("delete from test_table ") #this will delete everything from the table - if you want to specify what you need to be delete you will need where clause
conn.commit()
#really important is to commit every statement - otherwise it wont save the current transaction

#cur.execute("SELECT * from test_table")

#if we execute multiple time insert statement we would need to view only rows that are distincted - that usually is used to delete data that is replicated.
#cur.execute("with cte as (select row_number() over ( partition by name order by id) as rw, id , name from test_table) select id , name from cte where rw = 1")

#another approach to view only distincted result set is like this 
cur.execute("select distinct id, name from test_table")

#cur.fetchone() #returns only 1 row
#cur.fetchmany(4) #this will return the 4 rows from the result set
#cur.fetchall() #this will return all the results - within a list
print (cur.fetchall())
conn.commit()

conn.close()