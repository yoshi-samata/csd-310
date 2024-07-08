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

def show_films(cursor, title):
    # Method to execute an inner join on all tables
    # Iterate over the data set and output all results to the terminal window

    # Inner join query
    cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # Get results from cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # Iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


# Show the films with a title
show_films(cursor, "DISPLAYING FILMS")
# Close the cursor and database connection
cursor.close()
db.close()

