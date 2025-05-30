import mysql.connector

db_name = "my_db"

mydbConnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = db_name
)

myCursor = mydbConnection.cursor()

sqlQuery = """
            CREATE TABLE STUDENT(
                roll INT PRIMARY KEY,
                name VARCHAR(100)
            )
          """


myCursor.execute(sqlQuery)