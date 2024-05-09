-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT
    `city`, avg(`value`) AS avg_temp
FROM temperatures
GROUP by
    `city`
ORDER BY
    `avg_temp` DESC;
