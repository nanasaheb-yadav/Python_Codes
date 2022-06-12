<--INNET JOIN
SELECT *
FROM Table_A
JOIN Table_B;

<-- left join
SELECT *
FROM Table_A A
LEFT JOIN Table_B B
ON A.col = B.col;

<--right join
SELECT *
FROM Table_A A
RIGHT JOIN Table_B B
ON A.col = B.col;

<--full outer join
SELECT *
FROM Table_A A
FULL JOIN Table_B B
ON A.col = B.col;

<-- self joins

SELECT  A.emp_id AS "Emp_ID",A.emp_name AS "Employee",
        B.emp_id AS "Sup_ID",B.emp_name AS "Supervisor"
FROM employee A, employee B
WHERE A.emp_sup = B.emp_id;


select a.name as n1, b.name as n2, a.city as city
from A a, A b
where
a.city = b.city;

select * from A a
INNER JOIN B b
ON a.id = b.id;