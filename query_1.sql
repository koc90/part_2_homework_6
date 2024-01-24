-- query_1.sql
--5 uczniów z najwyższą średnią ocen ze wszystkich przedmiotów. (zakładam, że chodzi po prostu o średnią ze wszystkich posiadanych ocen)
SELECT students.full_name, avg(grades.mark) as TotalAverage
FROM grades INNER JOIN students ON grades.student_id = students.student_id
GROUP BY full_name
ORDER BY TotalAverage DESC 
LIMIT 5