SELECT A.CAR_ID, ROUND(AVG(DATEDIFF(A.END_DATE, A.START_DATE)+1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A
GROUP BY A.CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, A.CAR_ID DESC;