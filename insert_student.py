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
            INSERT INTO STUDENT(roll,name)
            VALUES(1001,"SHAHIN")
           """

myCursor.execute(sqlQuery)
myDBConnection.commit() # need to commit the changes in db

print("inserted successfully")