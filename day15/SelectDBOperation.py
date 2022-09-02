# Select
import mysql.connector

try:
    # Establish the connection to database using all the credentials
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")  #Returns a connection object
    curs = con.cursor()                         #Create cursor (temporary area or buffer)
    curs.execute("select * from student")       #Execute query through cursor
    # All records will be in cursor curs
    for row in curs:
        print(row[0], row[1])       # Print records

    con.close()                     #close the connection
except:
    print("Connection Unsuccessful!")

print("Finish")

