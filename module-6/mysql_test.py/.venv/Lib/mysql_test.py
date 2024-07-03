import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': 'Qxysti734!',
    'host': 'localhost',
    'database': 'movies'

}

# Test connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username or password is invalid!")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not")

    else:
        print(err)
finally:
    db.close()