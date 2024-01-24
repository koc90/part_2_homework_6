# Before executing python main.py you should call docker-compose up -d on command prommt

import psycopg2
from process_data_from_queries import PROCESS_DATA_FROM_QUERY

import prepare_database


NUMER_NOT_EMPTY_QUERIES = 11

SQL_QUERIES = [f"query_{str(i)}.sql" for i in range(NUMER_NOT_EMPTY_QUERIES)]

URI = "postgresql://worker:secret@localhost:5432/superblog"

SQL_CREATE_FILE = "create_tables.sql"

SQL_INSERT_FILES = [
    "insert_students.sql",
    "insert_groups.sql",
    "insert_lecturers.sql",
    "insert_subjects.sql",
    "insert_grades.sql",
]

# print(SQL_QUERIES)


def input_file_execute(file):
    with open(file, "r") as sql_file:
        sql = sql_file.read()
        print(sql, "\n")

    with psycopg2.connect(URI) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)


def output_file_execute(file):
    with open(file, "r") as sql_file:
        sql = sql_file.read()
        print(sql, "\n")

    with psycopg2.connect(URI) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

    return result


def create_tables():
    input_file_execute(SQL_CREATE_FILE)


def insert_data():
    for file in SQL_INSERT_FILES:
        input_file_execute(file)


def create_empty_sql_query(num):
    file = f"query_{str(num)}.sql"

    try:
        with open(file, "r") as f:
            contents = f.readlines()

        if len(contents) < 2:
            with open(file, "w") as f:
                f.write(f"-- {file}")
        for row in contents:
            print(row)
    except:
        with open(file, "w") as f:
            f.write(f"-- {file}")


def create_empty_sql_queries(s, e):
    for i in range(s, e):
        create_empty_sql_query(i)


def execute_queries(num):
    result = output_file_execute(SQL_QUERIES[num])
    return result


def main():
    create_tables()
    insert_data()
    create_empty_sql_queries(0, 4)
    res = []

    with open("results.txt", "w") as res_file:
        for i in range(NUMER_NOT_EMPTY_QUERIES):
            res.append(execute_queries(i))
            print(f"    query_{i}.sql result:")
            print(f"    query_{i}.sql result:", file=res_file)
            for row in res[i]:
                print(row)
                print(row, file=res_file)
            print("")
            print("", file=res_file)
            print("Result after processing:")
            print("Result after processing:", file=res_file)
            PROCESS_DATA_FROM_QUERY[i](res[i], res_file)
            print("\n\n")
            print("\n\n", file=res_file)

    # process_data_from_query_1(res[1])
    # process_data_from_query_2(res[2])


if __name__ == "__main__":
    main()
