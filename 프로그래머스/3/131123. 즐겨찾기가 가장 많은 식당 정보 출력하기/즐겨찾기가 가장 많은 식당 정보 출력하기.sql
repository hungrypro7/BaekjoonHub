-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE FAVORITES in (select max(favorites)
                    from rest_info
                    group by food_type)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC