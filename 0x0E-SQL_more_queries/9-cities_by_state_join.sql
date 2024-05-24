-- Lists all cities in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id;
