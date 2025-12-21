-- Task 8: List all cities of California in the database hbtn_0d_usa (no JOIN).

-- List all cities of California
SELECT id, name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id;
