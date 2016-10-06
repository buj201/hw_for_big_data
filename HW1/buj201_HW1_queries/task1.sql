CREATE VIEW alltrips AS (
	SELECT *
	FROM trips t NATURAL JOIN fares f
   	ORDER BY medallion, hack_license, vendor_id, pickup_datetime, pickup_longitude
	);
    
SELECT * FROM alltrips;
    