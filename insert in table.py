# insert data into a table
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", port="3306",user="root",passwd="root",database = "ineuron_demo", use_pure = True)
    if(conn.is_connected()):
        query = "insert into ineuron values(0,'Full Stack Data Science','Full Stack Data Science Course by Sudhanshu Kumar',1,1)"
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Data inserted successfully")
        conn.close()
except Exception as e:
    print(e)
    conn.close()