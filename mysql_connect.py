import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(read_default_file="/Users/Maryam/.my.cnf")
    print("Successfully connected to MySQL database")
    conn.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(err)

