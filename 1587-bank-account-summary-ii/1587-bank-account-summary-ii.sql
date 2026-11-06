SELECT name, balance
FROM(
    SELECT DISTINCT U.name,SUM(T.amount) OVER (PARTITION BY T.account) AS balance
    FROM Users AS U
    JOIN Transactions AS T
    ON U.account = T.account
) t
WHERE balance > 10000