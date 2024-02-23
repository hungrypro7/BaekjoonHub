SELECT A.FLAVOR
FROM FIRST_HALF A JOIN JULY B ON A.FLAVOR = B.FLAVOR
GROUP BY A.FLAVOR
ORDER BY (A.TOTAL_ORDER+SUM(B.TOTAL_ORDER)) DESC
LIMIT 3