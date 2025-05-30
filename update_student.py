import mysql.connector

db_name = "my_db"

myDBConnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = db_name
)


myCursor = myDBConnection.cursor()

sqlQuery = """
            UPDATE STUDENT
            SET name = "SHAHIN MIA"
            WHERE ROLL = 1001
           """

myCursor.execute(sqlQuery)
myDBConnection.commit() # need to commit the changes in db

print("UPDATED successfully")