-- query_2.sql
--Uczeń z najwyższą średnią ocen z wybranego przedmiotu.
SELECT students.full_name, avg(grades.mark) as mathematics_average
FROM grades 
INNER JOIN students ON grades.student_id = students.student_id 
INNER JOIN subjects ON grades.subject_id = subjects.subject_id 
WHERE subject_name = 'Mathematics'
GROUP BY full_name
ORDER BY mathematics_average DESC
LIMIT 1