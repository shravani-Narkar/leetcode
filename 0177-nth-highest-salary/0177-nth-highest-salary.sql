CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM (
        SELECT id, salary,
        DENSE_RANK() OVER(ORDER BY salary desc) rn
        FROM Employee
        )t
      WHERE rn = N

  );
END