# printing all the names of existing databases
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", port="3306",user="root",passwd="root",use_pure=True)
    if(conn.is_connected()):
        query  ="SHOW DATABASES"
        cursor = conn.cursor()
        cursor.execute(query);
        allDBs = [i[0] for i in cursor.fetchall()]
        print(allDBs)
        conn.close()
    else:
        print("DB is not connected")
except Exception as e:
    conn.close()
    print(e)