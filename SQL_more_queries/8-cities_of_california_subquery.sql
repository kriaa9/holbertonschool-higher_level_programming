-- Lists all cities of California from the hbtn_0d_usa database
-- Uses a subquery instead of JOIN to find California's state id
-- The subquery selects the id from states where name is California
-- Results are sorted in ascending order by cities.id
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
