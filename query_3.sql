-- query_3.sql
--Średnia ocen w grupach dla wybranego przedmiotu.
SELECT group_sign, avg(grades.mark) as mathematics_average
FROM grades 
INNER JOIN groups ON grades.student_id = groups.student_id 
INNER JOIN subjects ON grades.subject_id = subjects.subject_id 
WHERE subject_name = 'Mathematics'
GROUP BY group_sign
ORDER BY group_sign
