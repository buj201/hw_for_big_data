SELECT medallion,
	CONCAT(FORMAT(100*    
		#NUMERATOR: Number of trips missing GPS coordinates
		(SUM(CASE
			WHEN (pickup_longitude = 0 AND
				pickup_latitude = 0 AND
				dropoff_latitude = 0 AND
				dropoff_longitude	= 0) 
			THEN 1 ELSE 0 END)
		/
		#Denominator: Number of trips
		COUNT(*))
    , 4),'%') AS percentage_of_trips
FROM trips T1
GROUP BY medallion
ORDER BY medallion;
