SELECT State, MAX(temperature) AS max_temperature
FROM temperature_data
GROUP BY State
ORDER BY State;