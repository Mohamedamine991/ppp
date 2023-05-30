import mysql.connector


# Create the database

connection = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1'
)

database_name = 'ppp'

cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE {database_name}")
cursor.close()

# Close the connection
connection.close()
