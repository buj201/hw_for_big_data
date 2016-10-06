SELECT grouped.medallion as medallion, grouped.pickup_datetime as pickup_datetime
FROM (
	SELECT medallion, pickup_datetime, COUNT(*) AS duplicated
	FROM fares
	GROUP BY medallion, pickup_datetime
    ) grouped
WHERE grouped.duplicated>1
ORDER BY medallion;