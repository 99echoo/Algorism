SELECT
    animal_id,
    name
FROM (
    SELECT
        i.animal_id,
        i.name,
        RANK() OVER (ORDER BY DATEDIFF(o.datetime, i.datetime) DESC) AS rank_num
    FROM ANIMAL_INS AS i
    JOIN ANIMAL_OUTS AS o
        ON i.animal_id = o.animal_id
) AS ranked
WHERE rank_num <= 2;