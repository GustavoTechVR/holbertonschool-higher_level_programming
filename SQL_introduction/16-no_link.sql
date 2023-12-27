-- File: 16-no_link.sql
-- Description: This script lists all records of the table second_table in the specified database,
-- excluding rows without a name value, and displaying the score and the name, ordered by descending score.

-- Select all records with a name value, displaying score and name, and order by score in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
