import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="mysql_usr",
    passwd="MSQL*WpD_125",
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE test_db")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)