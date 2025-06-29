import os
import mysql.connector
from mysql.connector import Error

try:
    # Get MySQL password from environment variable named MYSQL_PASSWORD
    mysql_password = os.getenv('MYSQL_PASSWORD')

    # Connect to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=mysql_password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
