
import sqlite3 as db

con = db.connect('buffalo.db')
curser = con.cursor() # for exceucte our command
curser.execute("delete from users")
curser.execute("insert into users select 'kevin','1234';")
curser.execute("insert into users select 'ashley','pass1';")
curser.execute("insert into users select 'jimmy','18634';")
curser.execute("insert into users select 'luis','dfgtd';")
curser.execute("insert into users select 'edward','oops122';")
con.commit() # this mother fucking is needed
con.close()
