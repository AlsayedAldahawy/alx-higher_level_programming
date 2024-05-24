-- Lists all genres from the database hbtn_0d_tvshows along with the number of
SELECT
    g.NAME AS genre,
    count(*) as number_of_shows
FROM
    tv_genres as g
    inner join tv_show_genres as g2 on g.id = g2.genre_id
group by
    genre
order by
    number_of_shows DESC;
