-- query_9.sql
-- Lista kursów, na które uczęszcza uczeń.
-- Zakładam, że uczeń uczęszcza na kurs jeśli ma wystawioną jakąkolwiek ocenę z niego

-- SELECT subject_id FROM grades
-- WHERE student_id = 1
-- GROUP BY subject_id
-- ORDER By subject_id


SELECT full_name, subject_name FROM 
    (((SELECT * FROM grades 
    WHERE student_id = 1) as grades
    INNER JOIN students ON grades.student_id = students.student_id)
    INNER JOIN subjects ON grades.subject_id = subjects.subject_id)
GROUP BY subject_name, full_name