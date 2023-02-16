-- lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id
