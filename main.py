import datetime

import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    conn = psycopg2.connect(dbname='test', user='postgres',
                            password='asdfghjkl1', host='localhost')

    # Курсор для выполнения операций с базой данных
    cursor = conn.cursor()

    # create_table_query = '''CREATE TABLE item(
    # item_id serial NOT NULL PRIMARY KEY,
    # item_name VARCHAR (100) NOT NULL,
    # purchase_time timestamp NOT NULL,
    # price INTEGER NOT NULL
    # );'''
    # cursor.execute(create_table_query)
    # conn.commit()
    # print('Table created')
# Table created
# Соединение с PostgreSQL закрыто
#     insert_into_table = '''INSERT INTO item(item_id, item_name, purchase_time, price) VALUES (%s, %s, %s, %s)'''
#     item_purchase_time = datetime.datetime.now()
#     item_tuple = (12, 'Keyboard', item_purchase_time, '1200')
#     cursor.execute(insert_into_table, item_tuple)
#     conn.commit()
#     print('Item added successfully')
#     Item added successfully
# Соединение с PostgreSQL закрыто

    # cursor.execute('''SELECT purchase_time FROM item WHERE item_id=12''')
    # putchase_datetime = cursor.fetchone()
    # print('DATE', putchase_datetime[0].date())
    # print('TIME', putchase_datetime[0].time())
# DATE 2022-09-29
# TIME 19:18:08.968730
# Соединение с PostgreSQL закрыто
    cursor.execute('''DELETE FROM item WHERE item_id = 12''')
    conn.commit()
    print('Deleted')

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
