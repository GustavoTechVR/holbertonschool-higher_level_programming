-- File: 101-avg_temperatures.sql
-- Description: This script displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

-- Select the average temperature by city, ordered by temperature in descending order
SELECT city, AVG(temperature) AS avg_temp
FROM your_table_name -- Replace 'your_table_name' with the actual name of your table
GROUP BY city
ORDER BY avg_temp DESC;
