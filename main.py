import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(dbname='test', user='postgres',
                            password='asdfghjkl1', host='localhost')

    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()
    # SQL-запрос для создания новой таблицы
    create_table = '''CREATE TABLE MOBILE 
    (ID INT PRIMARY KEY NOT NULL,
    MODEL TEXT NOT NULL,
    PRICE REAL);'''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table)
    conn.commit()
    print("Таблица успешно создана в PostgreSQL")


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
