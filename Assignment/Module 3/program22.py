
import sqlite3

con=sqlite3.connect("student.db")
cur=con.cursor()

cur.execute(
    "insert into student (id,name,age,email) values (?,?,?,?)",
(2,"gopal",23,"gopal@gmail.com")
)

con.commit()
con.close()


