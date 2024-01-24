-- query_8.sql
--Średnia ocen wystawionych przez wykładowcę z danego przedmiotu.
--
-- SELECT avg(mark), subject_id FROM grades
-- WHERE subject_id IN 
--     (SELECT subject_id FROM subjects
--     WHERE lecturer_id = 2 )
-- GROUP BY subject_id


SELECT full_name, subject_name, avg(mark)  FROM 
(SELECT * FROM grades
WHERE subject_id IN 
    (SELECT subject_id FROM subjects
    WHERE lecturer_id = 2 )) AS grades
    INNER JOIN subjects ON subjects.subject_id = grades.subject_id
    INNER JOIN lecturers ON lecturers.lecturer_id = subjects.lecturer_id

GROUP BY subject_name, full_name