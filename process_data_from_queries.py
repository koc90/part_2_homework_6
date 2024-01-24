def double_print(t, f, end="\n"):
    print(t, end=end)
    print(t, file=f, end=end)


def process_data_from_query_0(result_list: list[tuple], f):
    pass


def process_data_from_query_1(result_list: list[tuple], f):
    for one in result_list:
        double_print(f"{one[0]}, average: %.2f" % one[1], f)


def process_data_from_query_2(result_list: list[tuple], f):
    double_print(f"{result_list[0][0]}, average: %.2f" % result_list[0][1], f)


def process_data_from_query_5(result_list: list[tuple], f):
    lecturer = result_list[0][1]
    double_print(f"lecturer:\n     {lecturer}\nsubjects: ", f)
    for subject, lecturer in result_list:
        double_print(f"     {subject}", f)


def process_data_from_query_6(result_list: list[tuple], f):
    group = result_list[0][0]
    double_print(f"group:\n     {group}\nstudents: ", f)
    for group, student in result_list:
        double_print(f"     {student}", f)


def process_data_from_query_7(result_list: list[tuple], f):
    subject = result_list[0][0]
    group = result_list[0][1]
    double_print(f"subject: {subject}\ngroup: {group}", f)

    previous_student = ""
    for row in result_list:
        student = row[2]
        mark = row[3]

        if student == previous_student:
            pass
        else:
            double_print(f"\n    student: {student}\n    marks: ", end="", f=f)
            previous_student = student
        double_print(mark, end=", ", f=f)
    double_print("", f)


def process_data_from_query_8(result_list: list[tuple], f):
    lecturer = result_list[0][0]
    double_print(f"Lecturer: {lecturer}\nAverages of the grades given:", f=f)
    for row in result_list:
        double_print(f"    {row[1]}: %.2f" % row[2], f=f)


def process_data_from_query_9(result_list: list[tuple], f):
    student = result_list[0][0]
    double_print(f"Student: {student}\nCourses attended:", f)
    for row in result_list:
        double_print(f"    {row[1]}", f)


def process_data_from_query_10(result_list: list[tuple], f):
    lecturer = result_list[0][0]
    student = result_list[0][1]
    double_print(f"Student: {student}\nLecturer: {lecturer}\nCommon subjects:", f)
    for row in result_list:
        double_print(f"    {row[2]}", f)


PROCESS_DATA_FROM_QUERY = [
    process_data_from_query_0,
    process_data_from_query_1,
    process_data_from_query_2,
    process_data_from_query_1,
    process_data_from_query_1,
    process_data_from_query_5,
    process_data_from_query_6,
    process_data_from_query_7,
    process_data_from_query_8,
    process_data_from_query_9,
    process_data_from_query_10,
    process_data_from_query_0,
    process_data_from_query_0,
]
