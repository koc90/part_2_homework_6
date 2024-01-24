-- query_4.sql
--Średnia ocen dla wszystkich grup, uwzględniając wszystkie oceny.
SELECT group_sign, avg(grades.mark) as total_average
FROM grades 
INNER JOIN groups ON grades.student_id = groups.student_id 
INNER JOIN subjects ON grades.subject_id = subjects.subject_id 
GROUP BY group_sign
ORDER BY group_sign