import MySQLdb
import csv
import sys
conn = MySQLdb.connect(host="localhost", user="sammy", password="password", database="test", auth_plugin='mysql_native_password')

cursor = conn.cursor()
csv_data = csv.reader(open('Internlist.csv'))
header = next(csv_data)

print('Importing the CSV Files')
mycursor = conn.cursor()
a = "DROP TABLE test_task"
cursor.execute(a)
cursor.execute("CREATE TABLE test_task (Name VARCHAR(255), Terraform VARCHAR(255), Kubernetes VARCHAR(255), Ansible VARCHAR(255))")
for row in csv_data:
    print(row)
    
    sql = "INSERT INTO test_task (Name, Terraform, Kubernetes, Ansible) VALUES (%s, %s, %s, %s)"
    print(sql)
    cursor.execute(sql, row)

conn.commit()
cursor.close()
print('Done')
