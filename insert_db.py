import mysql.connector
import csv

mydb = mysql.connector.connect(
                          host="localhost",
                                            database='testCSV',
                                                              user='demo1',
                                                                                password='easypass')

print(mydb)
print("DB Connection established")

mycursor = mydb.cursor()

with open('tb1.csv','r') as file:
    csv_data = csv.reader(file)

    print("Insertion Starting")

    for row in csv_data:
        mycursor.execute('INSERT INTO tb1_csv(Age,Workclass,Income) VALUES (%s, "%s", "%s")',row)

mydb.commit()
mycursor.close()

print("Insertion Done")
