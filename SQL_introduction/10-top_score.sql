-- File: 10-top_score.sql
-- Description: This script lists all records of the table second_table in the specified database,
-- displaying both the score and the name, and ordering the records by score in descending order.

-- Select all records, displaying score and name, and order by score in descending order
SELECT score, name FROM second_table ORDER BY score DESC;

