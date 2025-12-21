-- 16. Say my name
-- Lists all records of second_table with a non-empty name, ordered by score DESC
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
