# функции БД для курсового проекта
# Катков Илья - "Магазин спортивных товаров"

# импорт библиотек
import sqlite3
import os

# ПУТЬ К БАЗЕ ДАННЫХ
path_db = "db.sqlite"


# подключение к базе
def connect_db(file_db):
    try:
        # подключение к db.sqlite
        conn = sqlite3.connect(file_db)
        return conn
    except Exception as ex:
        print("Ошибка поключения к БД: " + str(ex))


# закрываем подключение к базе
def close_db(conn):
    try:
        # закрываем соединение с db.sqlite
        conn.commit()
    except Exception as ex:
        print("Произошла ошибка при закрытии БД:" + str(ex))


# создаем базу
def create_db():
    try:
        # перезаписываем БД
        db_file = open(path_db, 'w')
        db_file.close()

        conn = connect_db(path_db)  # подключаемся к БД
        cursor = conn.cursor()
        # запросы для создания таблиц в db.sqlite
        cursor.execute(
            """PRAGMA foreign_keys=on""")  # связи между таблицами - ВКЛ.
        query_producers = """CREATE TABLE IF NOT EXISTS producers (
                            id INTEGER PRIMARY KEY,
                            name TEXT
                            )"""
        query_categories = """CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY,
                            name TEXT
                            )"""
        query_goods = """CREATE TABLE IF NOT EXISTS goods (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        category TEXT,
                        producer TEXT,
                        volume INTEGER,
                        price INTEGER,
                        FOREIGN KEY (category) REFERENCES categories(name),
                        FOREIGN KEY (producer) REFERENCES producers(name)
                        )"""
        query_cheques = """CREATE TABLE IF NOT EXISTS cheques (
                        id INTEGER PRIMARY KEY,
                        goods TEXT,
                        date TEXT,
                        price INTEGER
                        )"""

        # выполнение запросов на создание таблиц
        cursor.execute(query_producers)
        cursor.execute(query_categories)
        cursor.execute(query_goods)
        cursor.execute(query_cheques)

        # закрываем соединение к БД
        close_db(conn)

        print("База данных успешно создана!")
    except Exception as ex:
        print("Ошибка базы данных. " + str(ex))


# заполняем базу тестовыми данными
def fill_test():
    conn = connect_db(path_db)  # подключаемся к БД
    cursor = conn.cursor()

    # заполняем таблицу Поставщики
    for producer in [
                    "Спортак", "Физрук", "МегаСпорт", "SportLife", "Тренер",
                    "Нонстоп", "СТАРТ", "Пуск", "Жизнь", "Лайф",
                    "Спорт", "Runner", "Balls", "Finish", "Пробег",
                    "Стартер", "T-SHIRT", "Strike", "Tiger", "Short"]:
        query_producer = """INSERT INTO producers (name) VALUES('{0}')
        """.format(producer)
        cursor.execute(query_producer)

    # заполянем таблицу Категории
    for category in [
                    "Толстовки", "Футболки", "Спортивные штаны", "Тренажеры",
                    "Мячи", "Перчатки для бокса", "Кроссовки", "Носки",
                    "Спортивная еда", "Здоровая еда", "Аксессуары", "Шорты",
                    "Ветровки", "Куртки", "Шнурки", "Очки", "Самокаты",
                    "Ролики", "Велосипеды", "Коврики"]:
        query_category = """INSERT INTO categories (name) VALUES('{0}')
        """.format(category)
        cursor.execute(query_category)

    # заполняем таблицу Товары
    for good in [
                (
                    "Толстовка мужская серая", "Толстовки",
                    "Спортак", 10, 1300),
                (
                    "Футболка женская белая", "Футболки",
                    "Физрук", 10, 1000),
                (
                    "Штаны спортивные мужские черные", "Спортивные штаны",
                    "МегаСпорт", 10, 1450),
                (
                    "Велотренажер Easy", "Тренажеры",
                    "SportLife", 10, 12500),
                (
                    "Мяч футбольный", "Мячи",
                    "Тренер", 10, 700),
                (
                    "Перчатки для бокса красные", "Перчатки для бокса",
                    "Нонстоп", 10, 1300),
                (
                    "Кроссвоки женские белые", "Кроссовки",
                    "СТАРТ", 10, 1600),
                (
                    "Носки мужские черные", "Носки",
                    "Пуск", 10, 300),
                (
                    "Батончик ЭНЕРГИЯ", "Спортивная еда",
                    "Жизнь", 10, 100),
                (
                    "Батончик RUN", "Здоровая еда",
                    "Лайф", 10, 150),
                (
                    "Браслет наручный", "Аксессуары",
                    "Спорт", 10, 100),
                (
                    "Шотры мужские серые", "Шорты",
                    "Runner", 10, 1700),
                (
                    "Ветровка женская розовая", "Ветровки",
                    "Balls", 10, 2000),
                (
                    "Куртка мужская черная", "Куртки",
                    "Finish", 10, 4000),
                (
                    "Шнурки белые", "Шнурки",
                    "Пробег", 10, 150),
                (
                    "Очки для сноуборда", "Очки",
                    "Стартер", 10, 1900),
                (
                    "Самокат MEDIUM", "Самокаты",
                    "T-SHIRT", 10, 3800),
                (
                    "Ролики женские желтые", "Ролики",
                    "Strike", 10, 2800),
                (
                    "Велосипед MAXIMUM", "Велосипеды",
                    "Tiger", 10, 12500),
                ("Коврик для упражнений", "Коврики", "Short", 10, 1000)]:
        query_good = """INSERT INTO goods (name, category, producer, volume, price)
        VALUES ('{0}', '{1}', '{2}','{3}', '{4}')
        """.format(good[0], good[1], good[2], good[3], good[4])
        cursor.execute(query_good)

    print("База данных успешно заполнена!")
    close_db(conn)


# выбираем все товары
def select_goods():
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_goods = """SELECT * FROM goods"""
    cursor.execute(query_goods)

    goods = cursor.fetchall()
    close_db(conn)

    return goods


# выбираем все категории
def select_categories():
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_categories = """SELECT * FROM categories"""
    cursor.execute(query_categories)

    categories = cursor.fetchall()
    close_db(conn)

    return categories


# выбираем всех поставщиков
def select_producers():
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_producers = """SELECT * FROM producers"""
    cursor.execute(query_producers)

    producers = cursor.fetchall()
    close_db(conn)

    return producers


# выбираем все чеки
def select_cheques():
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_cheques = """SELECT * FROM cheques"""
    cursor.execute(query_cheques)

    cheques = cursor.fetchall()
    close_db(conn)

    return cheques


# добавление товара
def add_good(name, category, producer, volume, price):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_add_good = """INSERT INTO goods (name, category, producer, volume, price)
    VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')
    """.format(name, category, producer, volume, price)
    cursor.execute(query_add_good)

    print("Товар добавлен!")
    close_db(conn)


# добавление категории
def add_category(name):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_add_category = """INSERT INTO categories (name)
    VALUES ('{0}')""".format(name)
    cursor.execute(query_add_category)

    print("Категория добавлена!")
    close_db(conn)


# добавление поставщика
def add_producer(name):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_add_producer = """INSERT INTO producers (name)
    VALUES ('{0}')""".format(name)
    cursor.execute(query_add_producer)

    print("Поставщик добавлен!")
    close_db(conn)


# добавление чека
def add_cheque(goods, date, price):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_add_cheque = """INSERT INTO cheques (goods, date, price)
    VALUES ('{0}', '{1}', '{2}')""".format(goods, date, price)
    cursor.execute(query_add_cheque)

    print("Чек добавлен!")
    close_db(conn)


# обновление товара
def edit_good(name, category, producer, volume, price, id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_edit_good = """UPDATE goods SET name = '{0}', category = '{1}',
    producer = '{2}', volume = '{3}', price = '{4}' WHERE id = '{5}'
    """.format(name, category, producer, volume, price, id)
    cursor.execute(query_edit_good)

    print("Товар изменен!")
    close_db(conn)


# обновление категории
def edit_category(name, id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_edit_category = """UPDATE categories SET name = '{0}'
     WHERE id = '{1}'""".format(name, id)
    cursor.execute(query_edit_category)

    print("Категория изменена!")
    close_db(conn)


# обновление поставщика
def edit_producer(name, id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_edit_producer = """UPDATE producers SET name = '{0}'
     WHERE id = '{1}'""".format(name, id)
    cursor.execute(query_edit_producer)

    print("Поставщик изменен!")
    close_db(conn)


# удаление товара
def del_good(id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_del_good = """DELETE FROM goods WHERE id = {0}""".format(id)
    cursor.execute(query_del_good)

    print("Товар удален!")
    close_db(conn)


# удаление категории
def del_category(id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_del_category = """DELETE FROM categories WHERE id = {0}""".format(id)
    cursor.execute(query_del_category)

    print("Категория удалена!")
    close_db(conn)


# удаление поставщика
def del_producer(id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_del_producer = """DELETE FROM producers WHERE id = {0}""".format(id)
    cursor.execute(query_del_producer)

    print("Поставщик удален!")
    close_db(conn)


# удаление чека
def del_cheque(id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_del_cheque = """DELETE FROM cheques WHERE id = {0}""".format(id)
    cursor.execute(query_del_cheque)

    print("Чек удален!")
    close_db(conn)


# выбираем один чек
def select_cheque(id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_cheque = """SELECT * FROM cheques WHERE id = {0}""".format(id)
    cursor.execute(query_cheque)

    cheque = cursor.fetchall()
    close_db(conn)

    return cheque


# вычитаем количество купленных товаров
def minus_count(minus, id):
    conn = connect_db(path_db)
    cursor = conn.cursor()

    query_good = """SELECT * FROM goods WHERE id = {0}""".format(id)
    cursor.execute(query_good)
    old = cursor.fetchall()[0][4]
    new = old - minus
    query_minus_count = """UPDATE goods SET volume = {0} WHERE id = {1}
    """.format(new, id)
    cursor.execute(query_minus_count)

    close_db(conn)


if __name__ == "__main__":
    create_db()
    fill_test()
