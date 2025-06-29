# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server (no database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",      # 🔁 Replace with your MySQL username
            password="your_password"   # 🔁 Replace with your MySQL password
        )

        cursor = connection.cursor()

        # Attempt to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("✅ Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

    finally:
        # Ensure the cursor and connection are closed properly
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
