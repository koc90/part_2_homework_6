-- query_10.sql
--Lista kursów prowadzonych przez wybranego wykładowcę dla określonego ucznia.


SELECT lecturer_sub.full_name, student_sub.full_name, lecturer_sub.subject_name FROM
    (SELECT subject_name, full_name FROM subjects
    INNER JOIN 
        (SELECT * FROM lecturers
        WHERE lecturer_id = 1
        ) AS lect ON subjects.lecturer_id = lect.lecturer_id) AS lecturer_sub
    INNER JOIN
        (SELECT full_name, subject_name FROM 
            (((SELECT * FROM grades 
            WHERE student_id = 11) as grades
            INNER JOIN students ON grades.student_id = students.student_id)
            INNER JOIN subjects ON grades.subject_id = subjects.subject_id)
        GROUP BY subject_name, full_name) AS student_sub
        ON lecturer_sub.subject_name = student_sub.subject_name
    