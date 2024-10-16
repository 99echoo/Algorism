SELECT score_table.SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
FROM HR_EMPLOYEES e
JOIN (
    SELECT SUM(g.SCORE) AS SCORE, e.EMP_NO
    FROM HR_EMPLOYEES e
    JOIN HR_GRADE g ON e.EMP_NO = g.EMP_NO
    GROUP BY e.EMP_NO
) AS score_table ON e.EMP_NO = score_table.EMP_NO
WHERE score_table.SCORE = (
    SELECT MAX(SCORE)
    FROM (
        SELECT SUM(g.SCORE) AS SCORE
        FROM HR_GRADE g
        JOIN HR_EMPLOYEES e ON e.EMP_NO = g.EMP_NO
        GROUP BY e.EMP_NO
    ) AS subquery
);