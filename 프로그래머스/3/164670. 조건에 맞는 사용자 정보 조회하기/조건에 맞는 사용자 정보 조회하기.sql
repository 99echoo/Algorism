-- 코드를 입력하세요
SELECT b.WRITER_ID, u.NICKNAME, CONCAT(u.CITY,' ',u.STREET_ADDRESS1,' ',u.STREET_ADDRESS2) AS 전체주소, CONCAT(SUBSTRING(TLNO,1,3),'-',
                                                                                                    SUBSTRING(TLNO,4,4),'-',
                                                                                                    SUBSTRING(TLNO,8,4)) AS 전화번호
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_USER u ON b.WRITER_ID = u.USER_ID
GROUP BY WRITER_ID
HAVING COUNT(*) >= 3
ORDER BY USER_ID DESC;