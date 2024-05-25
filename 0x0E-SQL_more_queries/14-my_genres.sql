-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
SELECT
    tv_genres.name
FROM
    tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    inner join tv_shows on tv_shows.id = tv_show_genres.show_id
WHERE
    tv_shows.title = "Dexter";
