-- Lists all cities with their corresponding state names from hbtn_0d_usa
-- Uses INNER JOIN to combine cities and states tables on the foreign key
-- Displays: cities.id, cities.name, states.name
-- Results are sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
