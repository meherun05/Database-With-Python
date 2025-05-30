import mysql.connector

mydbConnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456"
)

print(mydbConnection)

db_name = "my_db"

myCursor = mydbConnection.cursor()

sqlQuery = "CREATE DATABASE "+db_name

myCursor.execute(sqlQuery)