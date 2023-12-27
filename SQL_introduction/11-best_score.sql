-- File: 11-best_score.sql
-- Description: This script lists all records with a score >= 10 in the table second_table
-- in the specified database, displaying both the score and the name, and ordering the records by score in descending order.

-- Select records with score >= 10, displaying score and name, and order by score in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
