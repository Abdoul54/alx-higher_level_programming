-- display max tempretature of each state
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;