-- query_7.sql
--Oceny uczniów w wybranej grupie z określonego przedmiotu.
--
-- it works but the results are less readable 
-- SELECT * FROM grades
-- WHERE student_id IN
--     (SELECT student_id FROM groups
--     WHERE group_sign = 'B')
-- AND subject_id IN
--     (SELECT subject_id FROM subjects
--     WHERE subject_name = 'Chemistry')


SELECT subject_name, group_sign, full_name, mark FROM 
    (((SELECT * FROM groups
    WHERE group_sign = 'B') AS choosen_group

    INNER JOIN students ON choosen_group.student_id = students.student_id)

    INNER JOIN grades ON choosen_group.student_id = grades.student_id)

    INNER JOIN subjects ON grades.subject_id = subjects.subject_id
    WHERE subject_name = 'Chemistry'

