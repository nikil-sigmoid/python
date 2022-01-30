import mysql.connector
import os

MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASS = os.environ["MYSQL_PASS"]

db = mysql.connector.connect(host='localhost', user=MYSQL_USER, passwd=MYSQL_PASS,
                             database='DBDemoPython')  # local host, host="127.0.0.1"

try:
    my_cursor = db.cursor()
    my_cursor.execute("select * from user")
    # result = my_cursor.fetchone()
    for i in my_cursor:
        print(i)
except:
    print("Error in connection")
finally:
    db.close()
