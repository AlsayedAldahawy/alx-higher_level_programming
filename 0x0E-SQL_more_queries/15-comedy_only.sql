-- Lists all comedy shows in the database hbtn_0d_tvshows.
SELECT
    s.title
FROM
    tv_shows AS s
    INNER JOIN tv_show_genres as sg ON s.id = sg.show_id
    INNER JOIN tv_genres AS g ON sg.genre_id = g.id
where
    g.name = "Comedy"
ORDER BY
    s.title;
