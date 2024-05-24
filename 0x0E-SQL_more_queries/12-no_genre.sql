-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
SELECT
    S.title,
    G.genre_id
FROM
    tv_shows AS S
    LEFT JOIN tv_show_genres AS G ON S.id = G.show_id
WHERE
    G.genre_id IS NULL
ORDER BY
    S.title,
    G.genre_id;
