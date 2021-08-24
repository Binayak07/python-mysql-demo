import csv
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", port=3306, database="ineuron_demo",user="root", password="root",use_pure=True)
    cursor = conn.cursor()
    cursor.execute("create table if not exists iEmployee(id int(10) primary key auto_increment,first_name varchar(200),last_name varchar(200),email varchar(200),gender varchar(10),ip_address varchar(200))")
    print("Table created.")
    with open("MOCK_DATA.csv",'r') as data:
        data_csv = csv.reader(data, delimiter='\n')
        for (ind,i) in enumerate(data_csv):
            if ind==0:
                continue;
            spl = tuple(i[0].split(','))
            qry="insert into iEmployee(id,first_name,last_name,email,gender,ip_address) values(%s,%s,%s,%s,%s,%s)"
            # print(qry)
            cursor.execute(qry,spl)
    conn.commit()
    conn.close()
except Exception as e:
    print(e)