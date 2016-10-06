SELECT passenger_count AS number_of_passengers, COUNT(*) AS num_trips
FROM trips
GROUP BY passenger_count
ORDER BY number_of_passengers;