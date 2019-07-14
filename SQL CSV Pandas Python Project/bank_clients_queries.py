import sqlite3

connection = sqlite3.connect('bank.db')
query_number = 1


def print_column_names(connection, table):
    print('column names')
    c = connection.cursor()
    c.execute("""PRAGMA table_info(""" + table + ")")
    table_info = c.fetchall()
    column_names = [e[1] for e in table_info]
    print(column_names)


print_column_names(connection, "clients")


def query(connection, query_number, sql_code):
    print("\nquery " + str(query_number))
    query_number += 1

    c = connection.cursor()
    c.execute(sql_code)
    print(c.fetchall())
    return query_number


sql_code = """SELECT * FROM clients WHERE "index" < 40 ORDER BY age, balance ASC LIMIT 5"""
query_number = query(connection=connection, query_number=query_number, sql_code=sql_code)

sql_code = """SELECT education AS ed, balance FROM clients 
              WHERE job IN('housemaid', 'entrepreneur', 'student') AND balance between 500 AND 2000"""
query_number = query(connection, query_number, sql_code)

sql_code = """SELECT job, SUM(balance) FROM clients GROUP BY job"""
query_number = query(connection, query_number, sql_code)

sql_code = """SELECT DISTINCT education FROM clients WHERE education LIKE '%r%a_y'"""
query_number = query(connection, query_number, sql_code)

sql_code = """SELECT DISTINCT age FROM clients WHERE education =
              (SELECT DISTINCT education FROM clients WHERE balance >30000)"""
query_number = query(connection, query_number, sql_code)

sql_code = """SELECT DISTINCT age FROM clients WHERE education =
              (SELECT DISTINCT education FROM clients WHERE balance >30000)"""
query_number = query(connection, query_number, sql_code)

connection.close()
