import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='avasoft'
)

print("Connection sucsessfully")

my_Cursor = mydb.cursor()
# summa
my_Cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT)")
print('Table Created Sucessfully')

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
val = ("Praveen", 21)

# my_Cursor.execute(sql, val)
# mydb.commit()   # save changes

# print(my_Cursor.rowcount, "record inserted.")
my_Cursor.execute("SELECT * FROM students")

result = my_Cursor.fetchall()

for row in result:
    print(row)
