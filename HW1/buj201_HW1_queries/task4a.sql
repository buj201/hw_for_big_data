SELECT 	vehicle_type,
		COUNT(*) as total_trips,
		SUM(fare_amount) AS total_revenue,
        CONCAT(FORMAT(100*AVG(tip_amount/fare_amount),18), '%') as avg_tip_percentage
FROM medallions M NATURAL JOIN fares F
GROUP BY vehicle_type
ORDER BY vehicle_type;