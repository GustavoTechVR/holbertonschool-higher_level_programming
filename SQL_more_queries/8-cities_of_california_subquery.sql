-- Task: List all cities of California using a subquery
-- File: 8-cities_of_california_subquery.sql

-- Select all cities of California
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
