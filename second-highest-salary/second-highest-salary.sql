# Write your MySQL query statement below

select (select distinct Salary from employee
                   order by Salary Desc
                   LIMIT 1, 1) as SecondHighestSalary