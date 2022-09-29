import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(dbname='test', user='postgres',
                            password='asdfghjkl1', host='localhost')

    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()

    # insert_query = '''INSERT INTO   mobile (ID, MODEL, PRICE) VALUES (1, 'IPHONE13', '2300')'''
    # cursor.execute(insert_query)
    # conn.commit()
    # print('Запись успешно вставлена')
    # cursor.execute('SELECT * FROM mobile')
    # record = cursor.fetchall()
    # print('Result', record)
#     Запись успешно вставлена
# Result [(1, 'IPHONE13', 2300.0)]
# Соединение с PostgreSQL закрыто

    # Выполнение SQL-запроса для обновления таблицы
    # update_query = """Update mobile set price = 1500 where id = 1"""
    # cursor.execute(update_query)
    # conn.commit()
    # count = cursor.rowcount
    # print(count, "Запись успешно удалена")
    # # Получить результат
    # cursor.execute("SELECT * from mobile")
    # print("Результат", cursor.fetchall())
# 1 Запись успешно удалена
# Результат [(1, 'IPHONE13', 1500.0)]
# Соединение с PostgreSQL закрыто

# Выполнение SQL-запроса для удаления таблицы
#     delete_query = '''DELETE from mobile where id = 1'''
#     cursor.execute(delete_query)
#     conn.commit()
#     count = cursor.rowcount
#     print(count, 'Deleted')
#     cursor.execute('SELECT * from mobile')
#     print('REsult', cursor.fetchall())
#     1 Deleted
# REsult []
# Соединение с PostgreSQL закрыто

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
