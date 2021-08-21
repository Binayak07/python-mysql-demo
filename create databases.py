# creating a database if it is not present
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", port="3306",user="root",passwd="root",use_pure=True)
    if(conn.is_connected()):
        query  ="SHOW DATABASES"
        cursor = conn.cursor()
        cursor.execute(query)
        allDBs = [i[0] for i in cursor.fetchall()]
        print(allDBs)
        if "ineuron_demo2" not in allDBs:
            query = "create database ineuron_demo2"
            cursor = conn.cursor()
            cursor.execute(query)
            print("Database created successfully")
        conn.close()
    else:
        print("DB is not connected")
except Exception as e:
    conn.close()
    print(e)