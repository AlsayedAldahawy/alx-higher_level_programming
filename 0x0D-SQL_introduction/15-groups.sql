-- Lists the number of records with the same score in the table second_table.
SELECT score, name
FROM second_table
GROUP BY score;
