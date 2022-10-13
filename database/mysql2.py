import mysql.connector
import csv
mycon = mysql.connector.connect(host = 'localhost',
                                user = 'root',
                                password = 'Root@123',
                                database = 'player')

print(mycon)
mycursor = mycon.cursor()

csv_file = open("titanic.csv","r")
csv_records = csv_file.readlines()

# # print(csv_records)
sql = "insert into employee(emp_name, designation, age, salary) values(%s,%s,%s,%s,%s,%s)"
#mycursor.execute(sql,)
values = []
for i in csv_records:
    print(i)
    tuple_1 = i.split(',')
    print(tuple_1)
    values.append(tuple(tuple_1))
    print(values)
    
    
mycursor.executemany(sql,values)
print(mycursor.rowcount,"record inserted")

mycon.commit()
mycon.close() 