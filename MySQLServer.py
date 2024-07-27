import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mypassword'
    )

    if connection.is_connected():
        print("Connection successful!")

    cursor = connection.cursor()
    # Create database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")
    finally:
        cursor.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
