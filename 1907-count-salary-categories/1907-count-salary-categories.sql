# Write your MySQL query statement below
WITH c AS (
    SELECT IFNULL(SUM(income < 20000), 0) AS low,
           IFNULL(SUM(income BETWEEN 20000 AND 50000), 0) AS mid,
           IFNULL(SUM(income > 50000), 0) AS high
    FROM Accounts
)
SELECT 'Low Salary' AS category, low AS accounts_count FROM c
UNION ALL
SELECT 'Average Salary', mid FROM c
UNION ALL
SELECT 'High Salary', high FROM c;