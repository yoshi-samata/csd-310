/*
    Title: db_init_2022.sql
    Author: Professor Sampson
    Date: 1 Aug 2022
    Description: movies database initialization script.
*/

-- drop database user if exists 
DROP USER IF EXISTS 'movies_user'@'localhost';


-- create movies_user and grant them all privileges to the movies database 
CREATE USER 'movies_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'popcorn';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON movies.* TO 'movies_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS studio;


-- create the studio table 
CREATE TABLE studio (
    studio_id     INT             NOT NULL        AUTO_INCREMENT,
    studio_name   VARCHAR(75)     NOT NULL,
     
    PRIMARY KEY(studio_id)
); 


-- create the film table and set the foreign key
CREATE TABLE film (
    film_id   INT             NOT NULL        AUTO_INCREMENT,
    film_name  VARCHAR(75)     NOT NULL,
    film_releaseDate   VARCHAR(5)     NOT NULL,
	film_runtime INT NOT NULL,
	film_director VARCHAR(75) NOT NULL,
	studio_id INT NOT NULL,
	genre_id INT NOT NULL,
    PRIMARY KEY(film_id),
	CONSTRAINT fk_studio
    FOREIGN KEY(studio_id)
        REFERENCES studio(studio_id),
    CONSTRAINT fk_genre
    FOREIGN KEY(genre_id)
        REFERENCES genre(genre_id)	
);


-- insert movie records 
	INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
    VALUES('Gladiator', '2000', '155', 'Ridley Scott', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),(SELECT genre_id FROM genre WHERE genre_name = 'Drama') );

    
