# demonstrates how to create a new table
import mysql.connector as connection

try:
    db = connection.connect(host="localhost", port=3306,user="root",passwd="root", database="ineuron_demo", use_pure=True)
    if(db.is_connected()):
        query = "CREATE TABLE ineuron(course_id INT auto_increment PRIMARY KEY, course_name VARCHAR(100), course_description VARCHAR(100), duration INT, isActive TINYINT(1) default 1)"
        cursor = db.cursor()
        cursor.execute(query)
        print("Table created successfully")
    else:
        print("DB is not connected")
    db.close()
except Exception as e:
    print(e)
    db.close()