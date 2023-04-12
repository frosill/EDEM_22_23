import mysql.connector
import time
import socket

ip = socket.gethostbyname(socket.gethostname())

def insert_data(table_name, data):

    try:
        connection = mysql.connector.connect(
            host=ip, #mi IP
            port=6033,
            user="db_user",
            password="admin",
            database="app_db"
        )

        cursor = connection.cursor()

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        cursor.execute(sql_query, tuple(data.values()))
        connection.commit()
        print("Data inserted successfully into table")

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL: ", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



'''
-- Creation of store table
CREATE TABLE IF NOT EXISTS store (
  store_id INT NOT NULL,
  name varchar(250) NOT NULL,
  city_id INT NOT NULL,
  PRIMARY KEY (store_id),
  CONSTRAINT fk_city
      FOREIGN KEY(city_id) 
	  REFERENCES city(city_id)
);
'''

time.sleep(20) # Wait 20 seconds to ensure db is running

store_data = {
    "store_id" : 1456,
    "name" : "Walmart",
    "city_id" : 783,
}

insert_data("store", store_data)
