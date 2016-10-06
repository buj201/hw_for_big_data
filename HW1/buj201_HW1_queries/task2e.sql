SELECT medallion, COUNT(*) AS num_trips
FROM fares
GROUP BY medallion
ORDER BY medallion;