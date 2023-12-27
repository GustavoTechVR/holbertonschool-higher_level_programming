-- File: 12-no_cheating.sql
-- Description: This script updates the score of Bob to 10 in the table second_table
-- using only the name field in the specified database.

-- Update the score of Bob to 10
UPDATE second_table SET score = 10 WHERE name = 'Bob';
