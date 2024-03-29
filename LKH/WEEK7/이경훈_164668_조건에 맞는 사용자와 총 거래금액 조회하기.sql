SELECT USER_ID, NICKNAME, SUM(PRICE) TOTAL_SALES
FROM USED_GOODS_BOARD, USED_GOODS_USER
WHERE STATUS='DONE' AND USER_ID = WRITER_ID
GROUP BY WRITER_ID 
HAVING SUM(PRICE)>=700000
ORDER BY TOTAL_SALES;