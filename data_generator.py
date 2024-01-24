from datetime import datetime, timedelta
import faker
from random import randint


GROUP_SIGNS = ("C", "A", "B")
NUMBER_STUDENTS = 50
NUMBER_LECTURERS = 5
MARKS = (2.0, 3.0, 3.5, 4.0, 4.5, 5.0)

SUBJECTS = [
    "Mathematics",
    "Physics",
    "Mechanics",
    "Information Technology",
    "Chemistry",
    "Descriptive Geomery",
    "Numerical Methods",
]

fake_data = faker.Faker()

# print(fake_data.name())


def generate_fake_persons(num_persons: int) -> list:
    fake_persons = []
    for _ in range(num_persons):
        fake_person = fake_data.name()
        fake_persons.append(fake_person)

    return fake_persons


def genarate_fake_students() -> list:
    return generate_fake_persons(NUMBER_STUDENTS)


def genarate_fake_lecturers() -> list:
    return generate_fake_persons(NUMBER_LECTURERS)


def create_data_to_persons_table(generate_fake_persons) -> list[tuple]:
    # student_id, full_name
    person_names = generate_fake_persons()
    persons_table = []

    counter = 1
    for person in person_names:
        row = (counter, person)
        persons_table.append(row)
        counter += 1

    return persons_table


def create_data_to_group_table(student_table: list[tuple]) -> list[tuple]:
    students_in_group = round(NUMBER_STUDENTS / len(GROUP_SIGNS))
    group_table = []

    for student in student_table:
        group_num = student[0] % len(GROUP_SIGNS)
        row = (GROUP_SIGNS[group_num], student[0])
        group_table.append(row)

    group_table.sort()

    return group_table


def create_data_to_subject_table(lecturer_table: list[tuple]) -> list[tuple]:
    # subject_table = []

    # counter = 1
    # for subject in SUBJECTS:
    #     subj_num = counter - 1
    #     lect_num = subj_num % len(lecturer_table)
    #     row = (counter, subject, lecturer_table[lect_num][0])
    #     subject_table.append(row)
    #     counter += 1

    subject_table = [
        (1, SUBJECTS[0], 1),
        (2, SUBJECTS[1], 2),
        (3, SUBJECTS[2], 2),
        (4, SUBJECTS[3], 3),
        (5, SUBJECTS[4], 4),
        (6, SUBJECTS[5], 5),
        (7, SUBJECTS[6], 1),
    ]

    return subject_table


def create_list_of_dates() -> list[str]:
    list_of_dates = []
    classes_start = datetime(year=2023, month=10, day=2).date()

    for i in range(30):
        date = classes_start + timedelta(days=i)

        if date.weekday() not in [5, 6]:
            list_of_dates.append(str(date))

    # print(list_of_dates)
    return list_of_dates


def create_data_to_grade_table(
    student_table: list[tuple], subject_table: list[tuple]
) -> list[tuple]:
    list_of_dates = create_list_of_dates()
    grade_table = []
    counter = 1

    for student in student_table:
        for i in range(randint(16, 21)):
            row = (
                counter,
                MARKS[randint(0, len(MARKS) - 1)],
                list_of_dates[randint(0, len(list_of_dates) - 1)],
                student[0],
                subject_table[randint(0, len(subject_table) - 1)][0],
            )
            counter += 1
            grade_table.append(row)

    return grade_table


if __name__ == "__main__":
    student_table = create_data_to_persons_table(genarate_fake_students)
    print(f"student_table = {student_table}\n")
    group_table = create_data_to_group_table(student_table)
    print(f"group_table = {group_table}\n")
    lecturer_table = create_data_to_persons_table(genarate_fake_lecturers)
    print(f"lecturer_table = {lecturer_table}\n")
    subject_table = create_data_to_subject_table(lecturer_table)
    print(f"subject_table = {subject_table}\n")
    grade_table = create_data_to_grade_table(student_table, subject_table)
    print(f"grade_table = {grade_table}\n")
