USE directors_movies_schema;

-- INSERT INTO movies (genre,title,release_date,box_office,director_id)
-- VALUE('sci-fi','Back to the future','1987-03-09',347000000,1);

-- INSERT INTO movies (genre,title,release_date,box_office,director_id)
-- VALUE('sci-fi','Interstellar','2015-08-02',347000000,3);

UPDATE movies
SET box_office = 239000000
WHERE id = 2;

SELECT * FROM movies;
