-- Displays the average temperature (in Fahrenheit)
SELECT city, avg(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp desc;
