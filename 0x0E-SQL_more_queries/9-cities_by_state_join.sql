-- This script lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
SELECT c.id, c.name AS name, s.name AS name
FROM cities AS c
JOIN states AS s
ON c.state_id = s.id
ORDER BY c.id;
