# insert into users (username, password, email) values
from data_generator import (
    create_data_to_persons_table,
    create_data_to_group_table,
    create_data_to_persons_table,
    create_data_to_subject_table,
    create_data_to_grade_table,
    genarate_fake_students,
    genarate_fake_lecturers,
)


student_table = create_data_to_persons_table(genarate_fake_students)
group_table = create_data_to_group_table(student_table)
lecturer_table = create_data_to_persons_table(genarate_fake_lecturers)
subject_table = create_data_to_subject_table(lecturer_table)
grade_table = create_data_to_grade_table(student_table, subject_table)


def generate_insert_students_qsl_file():
    # DROP TABLE IF EXISTS students;
    # CREATE TABLE students (
    #     student_id INTEGER PRIMARY_KEY,
    #     full_name VARCHAR(255),
    # )

    with open("insert_students.sql", "w") as file:
        print("INSERT INTO students (student_id, full_name) VALUES", file=file)
        for student in student_table[0:-1]:
            print(f"{student},", file=file)

        print(f"{student_table[-1]}", file=file)


def generate_insert_groups_qsl_file():
    # DROP TABLE IF EXISTS groups;
    # CREATE TABLE groups (
    #     group_sign CHAR(1),
    #     student_id INTEGER,
    #     FOREIGN KEY (student_id) REFERENCES students (student_id)
    #         ON DELETE SET NULL
    #         ON UPDATE CASCADE
    # )

    with open("insert_groups.sql", "w") as file:
        print("INSERT INTO groups (group_sign, student_id) VALUES", file=file)
        for group in group_table[0:-1]:
            print(f"{group},", file=file)
        print(f"{group_table[-1]}", file=file)


def generate_insert_lecturers_qsl_file():
    # DROP TABLE IF EXISTS lecturers;
    # CREATE TABLE lecturers (
    #     lecturer_id INTEGER PRIMARY_KEY,
    #     lecturer_name VARCHAR(255)
    # )
    with open("insert_lecturers.sql", "w") as file:
        print("INSERT INTO lecturers (lecturer_id, full_name) VALUES", file=file)
        for lecturer in lecturer_table[0:-1]:
            print(f"{lecturer},", file=file)
        print(f"{lecturer_table[-1]}", file=file)


def generate_insert_subjects_qsl_file():
    # DROP TABLE IF EXISTS subjects;
    # CREATE TABLE subjects (
    #     subject_id INTEGER PRIMARY_KEY,
    #     subject_name VARCHAR(255) UNIQUE,
    #     lecturer_id INTEGER,
    #     FOREIGN KEY (lecturer_id) REFERENCES lecturers (lecturer_id)
    #         ON DELETE SET NULL
    #         ON UPDATE CASCADE
    # )
    with open("insert_subjects.sql", "w") as file:
        print(
            "INSERT INTO subjects (subject_id, subject_name, lecturer_id) VALUES",
            file=file,
        )
        for subject in subject_table[0:-1]:
            print(f"{subject},", file=file)
        print(f"{subject_table[-1]}", file=file)


def generate_insert_grades_qsl_file():
    # DROP TABLE IF EXISTS grades;
    # CREATE TABLE grades(
    #     grade_id INTEGER PRIMARY_KEY,
    #     mark FLOAT(1, 1),
    #     received_date DATE,
    #     student_id INTEGER,
    #     subject_id INTEGER,
    #     FOREIGN KEY (student_id) REFERENCES students (student_id)
    #         ON DELETE SET NULL
    #         ON UPDATE CASCADE,
    #     FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
    #         ON DELETE SET NULL
    #         ON UPDATE CASCADE
    # )
    with open("insert_grades.sql", "w") as file:
        print(
            "INSERT INTO grades (grade_id, mark, received_date, student_id, subject_id) VALUES",
            file=file,
        )
        for grade in grade_table[0:-1]:
            print(f"{grade},", file=file)
        print(f"{grade_table[-1]}", file=file)


def generate_all_insert_files():
    generate_insert_students_qsl_file()
    generate_insert_groups_qsl_file()
    generate_insert_lecturers_qsl_file()
    generate_insert_subjects_qsl_file()
    generate_insert_grades_qsl_file()


if __name__ == "__main__":
    generate_all_insert_files()
