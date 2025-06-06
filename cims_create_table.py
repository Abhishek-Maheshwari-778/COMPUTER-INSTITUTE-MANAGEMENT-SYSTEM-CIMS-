import mysql.connector as sql 
conn=sql.connect(host='localhost',user='root',passwd='12345',database='cims')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create table cand_details(adm_no int primary key, candidate_name varchar(50), course_select varchar(20))')
print ('Table created')

