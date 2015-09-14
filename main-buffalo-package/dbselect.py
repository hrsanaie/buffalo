__author__ = 'root'
import sqlite3 as db
import os
os.system('clear')
conn = db.connect('buffalo.db')
conn.row_factory=db.Row # for interpreter don't show error for tuple as must be int index
curser = conn.cursor()
curser.execute('select username from users')
rows = curser.fetchall()

for row in rows:
    print ('%s'% row['username'])