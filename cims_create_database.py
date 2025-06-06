import mysql.connector as sql 
conn=sql.connect(host='localhost',user='root',passwd='123456')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create database cims')
print ('Database created')
