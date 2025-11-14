import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database ="College"
)
print("Database connected successfully")
cursor = con.cursor()
sql ="insert into student (id,name,age) values (%s,%s,%s)"
value = (1,"Sailesh",21)
cursor.execute(sql,value)
con.commit()
print(cursor.rowcount,"record inserted")
cursor.close()
con.close()