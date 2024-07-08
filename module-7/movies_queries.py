import mysql.connector

# Database configuration
config = {
    'user': 'root',
    'password': 'Qxysti734!',
    'host': 'localhost',
    'database': 'movies'
}

# Connecting to the database
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Function to execute a query and print results
def execute_query(query, description):
    cursor.execute(query)
    results = cursor.fetchall()
    print(description)
    for row in results:
        print(row)
    print("\n")

# Query 1: Select all fields from the studio table
query1 = "SELECT * FROM studio"
description1 = "Query 1: All fields from the studio table:"
execute_query(query1, description1)

# Query 2: Select all fields from the genre table
query2 = "SELECT * FROM genre"
description2 = "Query 2: All fields from the genre table:"
execute_query(query2, description2)

# Query 3: Select movie names with a run time   of less than two hours
query3 = "SELECT film_name FROM film WHERE film_runtime < 120"
description3 = "Query 3: Movie names with a run time of less than two hours:"
execute_query(query3, description3)

# Query 4: Get a list of film names and directors grouped by director
query4 = """
SELECT film_director, GROUP_CONCAT(film_name SEPARATOR ', ') AS movies
FROM film
GROUP BY film_director
"""
description4 = "Query 4: List of film names and directors grouped by director:"
execute_query(query4, description4)

# Close the cursor and the database connection
cursor.close()
db.close()