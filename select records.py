# selecting the records from a table.
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", port="3306",user="root",passwd="root", database="ineuron_demo", use_pure = True)
    
    if(conn.is_connected()):
        query ="select * from ineuron;"
        cursor=conn.cursor()
        cursor.execute(query)
        for data in cursor.fetchall():
            print(data)
        conn.close()
    else:
        print("DB is not connected")
except Exception as e:
    print(e)
    conn.close()
    
# data will be fetced as list of tuples
    
