import mysql.connector

mydb = mysql.connector.connect(
          host="localhost",
          database='testCSV',
          user='demo1',
          password='easypass'
              )

print(mydb)
print("Congrats DB object created")


mycursor = mydb.cursor()

mycursor.execute("select * from tb1_csv")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


mydb.commit()
mycursor.close()

