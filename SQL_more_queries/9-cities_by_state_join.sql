-- Task: List all cities with their corresponding state names using a JOIN
-- File: 9-cities_by_state_join.sql

-- Select all cities and their corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
