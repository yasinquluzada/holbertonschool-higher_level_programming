-- 9. Full creation
-- Create second_table in the current database if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

-- Remove target rows to keep script idempotent
DELETE FROM second_table WHERE id IN (1, 2, 3, 4);

-- Insert required records
INSERT INTO second_table (id, name, score) VALUES
  (1, 'John', 10),
  (2, 'Alex', 3),
  (3, 'Bob', 14),
  (4, 'George', 8);
