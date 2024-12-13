import mysql.connector

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",  
        password=""    # Empty password
    )
    print("Successfully connected to MySQL")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")