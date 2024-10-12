SELECT 
    CONCAT(EXTRACT(QUARTER FROM DIFFERENTIATION_DATE), 'Q') AS QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER;