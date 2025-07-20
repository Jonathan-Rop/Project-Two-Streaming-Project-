WITH CTE AS (
  SELECT "Age" FROM "Health".records
  WHERE "Age" = 31
)
SELECT * FROM CTE;