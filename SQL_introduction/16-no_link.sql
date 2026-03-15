-- Lists all records of the table second_table excluding rows without a name value.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
