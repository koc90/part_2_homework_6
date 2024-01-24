-- table: students
DROP TABLE IF EXISTS students CASCADE;
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name VARCHAR(255)
);

-- table: groups
DROP TABLE IF EXISTS groups CASCADE;
CREATE TABLE groups (
    group_sign CHAR(1),
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (student_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- table: lecturer
DROP TABLE IF EXISTS lecturers CASCADE;
CREATE TABLE lecturers (
    lecturer_id INTEGER PRIMARY KEY,
    full_name VARCHAR(255)
);

-- table: subjects
DROP TABLE IF EXISTS subjects CASCADE;
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name VARCHAR(255) UNIQUE,
    lecturer_id INTEGER,
    FOREIGN KEY (lecturer_id) REFERENCES lecturers (lecturer_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


-- table: grades
DROP TABLE IF EXISTS grades CASCADE;
CREATE TABLE grades(
    grade_id INTEGER PRIMARY KEY,
    mark DECIMAL(2, 1),
    received_date DATE,
    student_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (student_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)