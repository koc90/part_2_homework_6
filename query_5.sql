-- query_5.sql
--Przedmioty, które prowadzi wybrany wykładowca.
SELECT subject_name, full_name FROM subjects
INNER JOIN 
    (SELECT * FROM lecturers
    WHERE lecturer_id = 1
    ) AS lect ON subjects.lecturer_id = lect.lecturer_id




