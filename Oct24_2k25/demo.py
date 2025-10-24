import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host = 'localhost',
        database = 'avasoft',
        user = 'root',
        password = 'root'
    )

    if connection.is_connected():
        print("Successfully connected to the database")

        cursor = connection.cursor()

        query = "select * from employee"

        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")