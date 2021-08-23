# to delete a record from a table
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost",port=3306,user="root",passwd="root", database="ineuron_demo", use_pure=True)
    query = "DELETE FROM ineuron WHERE course_id = 4;"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Record deleted");
    query = "SELECT * FROM ineuron;"
    cursor = conn.cursor()
    cursor.execute(query)
    print(cursor.fetchall())
    conn.close()
except Exception as e:
    print(e)