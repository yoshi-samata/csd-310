import mysql.connector

# Database configuration
config = {
    'user': 'root',  # replace with your username
    'password': 'Qxysti734!',  # replace with your password
    'host': 'localhost',
    'database': 'movies'
}

# Test connection
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Connection successful!")
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        for table in cursor.fetchall():
            print(table)
    connection.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")