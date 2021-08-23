import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", port=3306,user="root",passwd="root",database="ineuron_demo",use_pure=True)
    query = "UPDATE ineuron SET isActive = 1 WHERE course_id IN (2,3)"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("Data Updated")
    query = "SELECT * FROM ineuron"
    cursor.execute(query)
    print(cursor.fetchall())
    conn.close()
except Exception as e:
    print(e)