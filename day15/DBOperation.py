# Insert, Update, Delete
import mysql.connector

insert_query = "insert into student values(104, 'Kim')"
update_query = "update student set sname='Mary' where sid=104"
delete_query = "delete from student where sid=104"

try:
    # Establish the connection to database using all the credentials
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")  #Returns a connection object
    curs = con.cursor()             #Create cursor
    curs.execute(delete_query)      #Execute query through cursor
    con.commit()                    #commit transaction
    con.close()                     #close the connection
except:
    print("Connection Unsuccessful!")

print("Finish")

