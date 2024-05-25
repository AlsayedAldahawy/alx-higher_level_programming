-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
SELECT DISTINCT
    s.title
FROM
    tv_shows AS s
    LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
where
    s.id NOT IN(
        SELECT DISTINCT
            sg.show_id
        FROM
            tv_show_genres AS sg
            INNER JOIN tv_genres AS g ON g.id = sg.genre_id
        where
            g.name = "Comedy"
    )
ORDER BY s.title;
