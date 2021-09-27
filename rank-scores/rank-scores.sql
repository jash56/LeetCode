# Write your MySQL query statement below
select score, dense_rank () OVER (order by Score desc) as 'Rank' 
from Scores;