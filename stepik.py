# https://stepik.org/course/70710/

import datetime

import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(dbname='postgres', user='postgres',
                            password='asdfghjkl1', host='localhost')

    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()

    # create_table = '''CREATE TABLE Поросята(id SERIAL, вес INT, PRIMARY KEY(id));'''
    # cursor.execute(create_table)

    # insert_into_table = '''INSERT INTO Поросята(вес) VALUES (100), (200), (300);'''
    # cursor.execute(insert_into_table)

    # values = '''SELECT * FROM Поросята'''
    # cursor.execute(values)
    # conn.commit()
    # print('Result', cursor.fetchall())

    # create_new_table = '''CREATE TABLE Кормежка(номер_поросенка INT, FOREIGN KEY(номер_поросенка) REFERENCES Поросята(id));'''
    # cursor.execute(create_new_table)
    # conn.commit()
    # print('Table created')

    # insert_into_table = '''INSERT INTO Кормежка(номер_поросенка) VALUES ((SELECT COUNT(*) FROM Поросята));'''
    # cursor.execute(insert_into_table)
    # conn.commit()
    # print('Inserted')

    # drop = '''DROP TABLE Поросята, Кормежка'''
    # cursor.execute(drop)
    # conn.commit()
    # print('Done')

    # create_table1 = '''CREATE TABLE Поросята(id SERIAL, вес INT, PRIMARY KEY(id), CHECK(вес >= 0));'''
    # cursor.execute(create_table1)
    # conn.commit()
    # print('Создана 1 табл')
    # create_table2 = '''CREATE TABLE Кормежка(номер_поросенка INT, FOREIGN KEY(номер_поросенка) REFERENCES Поросята(id));'''
    # cursor.execute(create_table2)
    # conn.commit()
    # print('Создана 2 табл')
    #
    # command1 = '''BEGIN; INSERT INTO Поросята(вес) VALUES (100);  INSERT INTO Кормежка(номер_поросенка) VALUES ((SELECT COUNT(*) FROM Поросята)); COMMIT;'''
    # cursor.execute(command1)
    # command2 = '''BEGIN; INSERT INTO Поросята(вес) VALUES (200);  INSERT INTO Кормежка(номер_поросенка) VALUES ((SELECT COUNT(*) FROM Поросята)); COMMIT;'''
    # cursor.execute(command2)
    # command3 = '''BEGIN; INSERT INTO Поросята(вес) VALUES (-300);  INSERT INTO Кормежка(номер_поросенка) VALUES ((SELECT COUNT(*) FROM Поросята)); COMMIT;'''
    # cursor.execute(command3)
    # command4 = '''BEGIN; INSERT INTO Поросята(вес) VALUES (300);  INSERT INTO Кормежка(номер_поросенка) VALUES ((SELECT COUNT(*) FROM Поросята)); COMMIT; '''
    # cursor.execute(command4)
    # conn.commit()

    com = '''SELECT * FROM  Поросята'''
    cursor.execute(com)
    conn.commit()
    print('Result', cursor.fetchall())


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
