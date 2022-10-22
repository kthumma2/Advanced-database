import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3. connect("Phones_list.db")

cursor = connection. cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Apple')")
cursor.execute("insert into list (description) values ('Samsung')")
cursor.execute("insert into list (description) values ('Nokia')")
cursor.execute("insert into list (description) values ('Motorola')")
cursor.execute("insert into list (description) values ('Google Pixel')")

connection.commit()
connection.close()

print("done.")
