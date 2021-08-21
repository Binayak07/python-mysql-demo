import mysql.connector as connection
import pandas as pd

try:
    conn = connection.connect(host="localhost", port=3306, user="root", passwd="root",database="ineuron_demo",use_pure=True)
    if (conn.is_connected()):
        query = "select * from ineuron"
        result_dataframe = pd.read_sql(query,conn)
        print(result_dataframe)
        conn.close()
    else:
        print("DB is not connected")
except Exception as e:
    print(e)
    conn.close()