import csv
import pandas as pd
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", port=3306, database="ineuron_demo",user="root", password="root",use_pure=True)
    cursor = conn.cursor()
    cursor.execute("create table if not exists iEmployee(id int(10) primary key auto_increment,first_name varchar(200),last_name varchar(200),email varchar(200),gender varchar(10),ip_address varchar(200))")
    print("Table created.")
    with open("MOCK_DATA.csv",'r') as data:
        next(data)
        data_csv = csv.reader(data, delimiter="\n")
        for i in enumerate(data_csv):
            for j in i[1]:
                cursor.execute("insert into iEmployee values({DATA})".format(DATA=j))
    conn.commit()
    conn.close()
except Exception as e:
    print(e)