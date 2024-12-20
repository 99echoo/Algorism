-- 코드를 입력하세요
SELECT C.FLAVOR
FROM (SELECT B.FLAVOR, SUM(B.TOTAL_ORDER + A.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF B
LEFT JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM JULY
GROUP BY FLAVOR) A ON B.FLAVOR = A.FLAVOR
GROUP BY B.FLAVOR
ORDER BY TOTAL_ORDER DESC) C
LIMIT 3