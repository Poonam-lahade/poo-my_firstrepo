import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root"
)  
  
cursor = myconn.cursor()

# Show existing tables
cursor.execute("SHOW TABLES")

for x in cursor:
  print(x) 