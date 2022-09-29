import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(dbname='test', user='postgres',
                            password='asdfghjkl1', host='localhost')

    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(conn.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
