SELECT city, MAX(temperature) AS max_temperature
FROM temperature_data
WHERE (month = 7 OR month = 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;