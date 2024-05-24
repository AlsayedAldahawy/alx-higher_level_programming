-- Lists all genres from the database hbtn_0d_tvshows along with the number of
SELECT
    g.NAME AS genre,
    count(*) AS number_of_shows
FROM
    tv_genres as g
    INNER JOIN tv_show_genres AS g2 ON g.id = g2.genre_id
GROUP BY
    genre
ORDER BY
    number_of_shows DESC;
