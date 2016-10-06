SELECT DATE(pickup_datetime) AS `day`, SUM(total_amount) AS total_revenue
FROM fares
GROUP BY `day`
ORDER BY `day`;