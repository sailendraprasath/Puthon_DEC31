import mysql.connector

# First connect without specifying database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  # empty for XAMPP
)
cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
cursor.close()
conn.close()

# Now connect to that database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
)
""")
print("✅ Table created successfully.")

cursor.close()
conn.close()
