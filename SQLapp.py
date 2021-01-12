import mysql.connector as sql
import flask 

db=sql.connect(
host="localhost",
user="root",password="root",database='test')

cur=db.cursor()

cur.execute("SHOW TABLES")

for i in cur.fetchone():
    print(i)