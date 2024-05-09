-- displays the max temperature of each state (ordered by State name).
-- state   max_temp
-- AZ  110
-- CA  110
-- IL  110
SELECT
    `state`,
    MAX(`value`) AS max_temp
FROM
    temperatures
GROUP BY
    `State`
ORDER BY
    `state`
