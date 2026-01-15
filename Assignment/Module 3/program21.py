# 21) Write a Python program to create a database and a table using SQLite3.

import sqlite3

con=sqlite3.connect("student.db")

cur=con.cursor()

# cur.execute("create table student (id int primary key,name varchar(50),age varchar(3),email varchar(50))")



cur.execute("insert into student (id,name,age,email) values (?,?,?,?)",
(1,"parth",20,"parth@gmail.com")
)


con.commit()
con.close()