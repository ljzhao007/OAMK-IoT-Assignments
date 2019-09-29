import mysql.connector as mysql

# Connect to Database

db = mysql.connect(
    host="arpad.ga",
    user="oamk",
    passwd="oamk",
    database="oamk"
)

cursor = db.cursor()

# Create Database

cursor.execute("CREATE DATABASE oamk")

# Create Table

cursor.execute("""
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE
  )
""")

# Insert Data

sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
data = [
    ('arpad', 'arpad@mail.com'),
    ('alexa', 'alexa@mail.ru')
]

cursor.executemany(sql, data)
db.commit()

# Select Data

select_all = "SELECT * FROM users"
cursor.execute(select_all)
query_result = cursor.fetchall()

for result in query_result:
    print(result)
