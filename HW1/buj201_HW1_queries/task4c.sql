SELECT 	agent_name, SUM(fare_amount) AS total_revenue
FROM medallions M JOIN fares F ON (M.medallion = F.medallion)
GROUP BY agent_number
ORDER BY total_revenue desc, agent_name
LIMIT 10;