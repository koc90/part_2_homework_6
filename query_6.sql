-- query_6.sql
--Lista uczniów w wybranej grupie.
SELECT group_sign, full_name FROM
groups INNER JOIN students ON groups.student_id = students.student_id
WHERE group_sign = 'C'