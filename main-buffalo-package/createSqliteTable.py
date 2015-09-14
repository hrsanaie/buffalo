__author__ = 'root'
import sqlite3 as db

conn = db.connect("buffalo.db")
curser = conn.cursor() # for execute the sql command or query
curser.execute("create table users (username text,password text)")
conn.close()
print ('table is created');