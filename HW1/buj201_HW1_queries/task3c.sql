SELECT hack_license, COUNT(DISTINCT medallion) as num_taxis_used
FROM trips
GROUP BY hack_license
ORDER BY hack_license;