-- Task: Create table force_name
-- File: 3-force_name.sql

-- Create table force_name if not exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
