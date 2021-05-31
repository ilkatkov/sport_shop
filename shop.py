# главное приложение для курсового проекта
# Катков Илья - "Магазин спортивных товаров"

# импорт библиотек
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functions import db
import datetime
import os


# вставка результата запроса в таблицу
def insert_in_table(query_func):
    for i in table.get_children():
        table.delete(i)
    for row in query_func:
        table.insert('', 'end', values=row)


# стиль таблицы
def style_table():
    table.grid_forget()
    table['show'] = "headings"
    table['height'] = 3
    style = ttk.Style(root)
    style.configure('Treeview', rowheight=78)


# выделяем запись
def select_item(item):
    choice = table.get_children()[int(item)-1]
    table.selection_set(choice)


# вывод товаров
def table_goods():
    table['columns'] = ("id", "name", "category",
                        "producer", "volume", "price")
    table.column("id", width=50, anchor=CENTER)
    table.column("name", width=220, anchor=CENTER)
    table.column("category", width=95, anchor=CENTER)
    table.column("producer", width=95, anchor=CENTER)
    table.column("volume", width=80, anchor=CENTER)
    table.column("price", width=60, anchor=CENTER)
    table.heading("id", text="ID")
    table.heading("name", text="Наименование")
    table.heading("category", text="Категория")
    table.heading("producer", text="Поставщик")
    table.heading("volume", text="Количество")
    table.heading("price", text="Цена")

    insert_in_table(db.select_goods())

    style_table()

    table.grid(row=1, column=1, rowspan=5)

    btn_add = Button(text="Добавить товар", width=18, command=add_good)
    btn_add.grid(row=1, column=2, sticky=W)

    btn_edit = Button(text="Изменить товар", width=18, command=edit_good)
    btn_edit.grid(row=2, column=2, sticky=W)

    btn_del = Button(text="Удалить товар", width=18, command=del_good)
    btn_del.grid(row=3, column=2, sticky=W)


# вывод категорий
def table_categories():
    table['columns'] = ("id", "name")
    table.column("id", width=50, anchor=CENTER)
    table.column("name", width=550, anchor=CENTER)
    table.heading("id", text="ID")
    table.heading("name", text="Категория")

    insert_in_table(db.select_categories())

    style_table()

    table.grid(row=1, column=1, rowspan=5)

    btn_add = Button(
        text="Добавить категорию", width=18,
        command=add_category)
    btn_add.grid(row=1, column=2, sticky=W)

    btn_edit = Button(
        text="Изменить категорию", width=18,
        command=edit_category)
    btn_edit.grid(row=2, column=2, sticky=W)

    btn_del = Button(
        text="Удалить категорию", width=18,
        command=del_category)
    btn_del.grid(row=3, column=2, sticky=W)


# вывод поставщиков
def table_producers():
    table['columns'] = ("id", "name")
    table.column("id", width=50, anchor=CENTER)
    table.column("name", width=550, anchor=CENTER)
    table.heading("id", text="ID")
    table.heading("name", text="Поставщик")

    insert_in_table(db.select_producers())

    style_table()
    table.grid(row=1, column=1, rowspan=5)

    btn_add = Button(
        text="Добавить поставщика", width=18,
        command=add_producer)
    btn_add.grid(row=1, column=2, sticky=W)

    btn_edit = Button(
        text="Изменить поставщика", width=18,
        command=edit_producer)
    btn_edit.grid(row=2, column=2, sticky=W)

    btn_del = Button(
        text="Удалить поставщика", width=18,
        command=del_producer)
    btn_del.grid(row=3, column=2, sticky=W)


# вывод чеков
def table_cheques():
    table['columns'] = ("id", "goods", "date", "price")
    table.column("id", width=50, anchor=CENTER)
    table.column("goods", width=325, anchor=CENTER)
    table.column("date", width=150, anchor=CENTER)
    table.column("price", width=75, anchor=CENTER)
    table.heading("id", text="ID")
    table.heading("goods", text="Товары")
    table.heading("date", text="Дата и время")
    table.heading("price", text="Сумма")

    for i in table.get_children():
        table.delete(i)
    for row in db.select_cheques():
        table.insert('', 'end', values=row)

    style_table()
    table.grid(row=1, column=1, rowspan=5)

    btn_add = Button(
        text="Добавить чек", width=18,
        command=add_cheque)
    btn_add.grid(row=1, column=2, sticky=W)

    btn_del = Button(
        text="Удалить чек", width=18,
        command=del_cheque)
    btn_del.grid(row=2, column=2, sticky=W)

    btn_print = Button(
        text="Распечатать чек", width=18,
        command=print_cheque)
    btn_print.grid(row=3, column=2, sticky=W)


# окно добавления товара
def add_good():
    add_window = Toplevel()
    add_window.geometry("300x300")
    add_window.iconbitmap("icon.ico")
    add_window.title("Добавить товар")
    add_window.resizable(0, 0)

    lbl_name = Label(add_window, text="Наименование:")
    lbl_name.grid(row=0, column=0, padx=20, pady=10, sticky=W)

    lbl_category = Label(add_window, text="Категория:")
    lbl_category.grid(row=1, column=0, padx=20, pady=10, sticky=W)

    lbl_producer = Label(add_window, text="Поставщик:")
    lbl_producer.grid(row=2, column=0, padx=20, pady=10, sticky=W)

    lbl_volume = Label(add_window, text="Количество:")
    lbl_volume.grid(row=3, column=0, padx=20, pady=10, sticky=W)

    lbl_price = Label(add_window, text="Цена:")
    lbl_price.grid(row=4, column=0, padx=20, pady=10, sticky=W)

    ent_name = Entry(add_window, width=25)
    ent_name.grid(row=0, column=1)
    ent_name.focus_set()

    category = StringVar(
        add_window)  # переменная для хранения выбора категории
    categories_temp = db.select_categories()  # берем данные из бд
    categories = []  # создаем список категорий

    # заполняем список категорий
    for i in categories_temp:
        categories.append(i[1])
    categories.sort()

    opt_category = OptionMenu(add_window, category, *categories)
    opt_category.grid(row=1, column=1)
    category.set(categories[0])  # выбрали категорию по умолчанию

    producer = StringVar(
        add_window)  # переменная для хранения выбора категории
    producers_temp = db.select_producers()  # берем данные из бд
    producers = []  # создаем список категорий

    # заполняем список поставщиков
    for i in producers_temp:
        producers.append(i[1])
    producers.sort()

    opt_producer = OptionMenu(add_window, producer, *producers)
    opt_producer.grid(row=2, column=1)
    producer.set(producers[0])  # выбрали поставщика по умолчанию

    ent_volume = Entry(add_window, width=25)
    ent_volume.grid(row=3, column=1)

    ent_price = Entry(add_window, width=25)
    ent_price.grid(row=4, column=1)

    # добавляем товар в БД
    def ok_click():
        if ent_name.get() == "":
            mb.showerror(
                "Добавить товар",
                "Введите наименование товара!")
            return ent_name.focus_set()
        for row in db.select_goods():
            if ent_name.get() in row:
                mb.showerror(
                    "Добавить товар",
                    "Товар с таким наименованием уже существует!")
                return ent_name.focus_set()
        if ent_volume.get() == "":
            mb.showerror(
                "Добавить товар",
                "Введите количество товара!")
            return ent_volume.focus_set()
        if ent_price.get() == "":
            mb.showerror(
                "Добавить товар",
                "Введите цену товара!")
            return ent_price.focus_set()
        try:
            db.add_good(
                ent_name.get(), category.get(),
                producer.get(), int(ent_volume.get()),
                int(ent_price.get()))
        except ValueError:
            mb.showerror(
                "Добавить товар",
                """Ввод количества и цены товара\n
осуществляется в числовом формате!""")
            return add_window.focus_set()
        table_goods()
        table.yview_moveto(1)
        add_window.destroy()

    btn_ok = Button(
        add_window, text="Добавить",
        width=10, command=ok_click)
    btn_ok.grid(row=5, column=0, pady=45, padx=5)

    btn_cancel = Button(
        add_window, text="Отмена",
        width=10, command=add_window.destroy)
    btn_cancel.grid(row=5, column=1, pady=45, padx=5)


# окно добавления категории
def add_category():
    add_window = Toplevel()
    add_window.geometry("300x100")
    add_window.resizable(False, False)
    add_window.title("Добавить категорию")
    add_window.iconbitmap("icon.ico")
    add_window.resizable(0, 0)

    lbl_category = Label(
        add_window, text="Категория:")
    lbl_category.grid(row=0, column=0, padx=20, pady=10, sticky=W)

    ent_category = Entry(add_window, width=25)
    ent_category.grid(row=0, column=1)
    ent_category.focus_set()

    # подтверждаем добавление категории
    def ok_click():
        if ent_category.get() == "":
            mb.showerror(
                "Добавить категорию",
                "Введите имя категории!")
            return ent_category.focus_set()
        for row in db.select_categories():
            if ent_category.get() in row:
                mb.showerror(
                    "Добавить категорию",
                    "Категория с таким именем уже существует!")
                return ent_category.focus_set()
        db.add_category(ent_category.get())
        table_categories()
        table.yview_moveto(1)
        add_window.destroy()

    btn_ok = Button(add_window, text="Добавить", width=10, command=ok_click)
    btn_ok.grid(row=5, column=0, pady=20, padx=5)

    btn_cancel = Button(
        add_window, text="Отмена",
        width=10, command=add_window.destroy)
    btn_cancel.grid(row=5, column=1, pady=20, padx=5)


# окно добавления поставщика
def add_producer():
    add_window = Toplevel()
    add_window.geometry("300x100")
    add_window.resizable(False, False)
    add_window.iconbitmap("icon.ico")
    add_window.title("Добавить поставщика")
    add_window.resizable(0, 0)

    lbl_producer = Label(add_window, text="Поставщик:")
    lbl_producer.grid(row=0, column=0, padx=20, pady=10, sticky=W)

    ent_producer = Entry(add_window, width=25)
    ent_producer.grid(row=0, column=1)
    ent_producer.focus_set()

    # подтверждаем добавление поставщика
    def ok_click():
        if ent_producer.get() == "":
            mb.showerror(
                "Добавить поставщика",
                "Введите имя поставщика!")
            return ent_producer.focus_set()
        for row in db.select_producers():
            if ent_producer in row:
                mb.showerror(
                    "Добавить поставщика",
                    "Поставщик с таким именем уже существует!")
                return ent_producer.focus_set()
        db.add_producer(ent_producer.get())
        table_producers()
        table.yview_moveto(1)
        add_window.destroy()

    btn_ok = Button(
        add_window, text="Добавить",
        width=10, command=ok_click)
    btn_ok.grid(row=5, column=0, pady=20, padx=5)

    btn_cancel = Button(
        add_window, text="Отмена",
        width=10, command=add_window.destroy)
    btn_cancel.grid(row=5, column=1, pady=20, padx=5)


# окно добавления чека
def add_cheque():
    goods = list(map(list, db.select_goods()))
    goods_names_ns = []
    for name in goods:
        goods_names_ns.append(name[1])
    goods_names = sorted(goods_names_ns)
    numbers = []
    for num in range(1, 11):
        numbers.append(str(num))

    # обнуляем итоговую цену при закрытии окна
    def close_add_cheque():
        global total
        total = 0
        add_window.destroy()

    add_window = Toplevel()
    add_window.geometry("480x275")
    add_window.resizable(False, False)
    add_window.iconbitmap("icon.ico")
    add_window.title("Добавить чек")
    add_window.focus_set()
    add_window.protocol("WM_DELETE_WINDOW", close_add_cheque)

    goods_var = StringVar(add_window)
    goods_var.set("Выберите товар")
    num_var = StringVar(add_window)
    num_var.set("1")

    # при выборе товара меняется кол-во на складе и цена за шт.
    def change_name(event):
        choice = goods_names_ns.index(goods_var.get())
        lbl_count['text'] = "Количество товара на складе: "
        lbl_count['text'] += str(goods[choice][4]) + " шт."
        lbl_price['text'] = "Цена за шт.: " + str(goods[choice][5])
        num_var.set("1")

    lbl_good = Label(
        add_window, text="Наименование товара:")
    lbl_good.grid(row=0, column=0, padx=10, sticky=W)
    goods_option = OptionMenu(
        add_window, goods_var,
        *goods_names, command=change_name)
    goods_option.grid(row=0, column=1,  pady=10)
    lbl_count = Label(
        add_window, text="Количество товара на складе: - шт.",
        width=28)
    lbl_count.grid(row=1, column=0, padx=10, sticky=W)
    lbl_num = Label(
        add_window, text="Продано шт.:")
    lbl_num.grid(row=2, column=0, padx=10, sticky=W)
    num_option = OptionMenu(
        add_window, num_var,
        *numbers)
    num_option.grid(row=2, column=0,  pady=10, padx=90)
    lbl_price = Label(
        add_window, text="Цена за шт.:")
    lbl_price.grid(row=3, column=0, padx=10, sticky=W)

    lbl_total = Label(
        add_window, text="Итого:")
    lbl_total.grid(row=4, column=0, padx=10,  pady=10, sticky=W)

    textarea = Text(
        add_window, width=26,
        height=10, state=DISABLED)
    textarea.grid(row=1, column=1, rowspan=5)

    # добавление позиции в чек
    def add_row():
        global total
        global goods_list
        global volume_list
        choice = goods_names_ns.index(goods_var.get())

        # если кол-во купленных товаров больше, чем имеется на складе,
        # то выдаем уведомление об этом
        if int(num_var.get()) > goods[choice][4]:
            mb.showerror(
                "Добавить чек",
                """Количество проданных товаров превышает
количество товаров на складе!""")
            num_var.set("1")
            add_window.focus_set()
        else:
            last_row = goods_var.get()
            last_price = goods[choice][5] * int(num_var.get())
            textarea.config(state=NORMAL)
            new_row = last_row[0:13] + ". " + str(goods[choice][5]) + " * "
            new_row += num_var.get() + " = " + str(last_price) + "\n"
            textarea.insert(END, new_row)
            textarea.config(state=DISABLED)
            goods[choice][4] = goods[choice][4] - int(num_var.get())
            lbl_count['text'] = "Количество товара на складе: "
            lbl_count['text'] += str(goods[choice][4]) + " шт."
            total += goods[choice][5] * int(num_var.get())

            lbl_total['text'] = "Итого: " + str(total)

            goods_list.append(choice)
            volume_list.append(int(num_var.get()))

    # добавляем чек в БД и вычитаем число купленных товаров из имеющихся
    def new_cheque():
        global total
        global goods_list
        global volume_list
        if textarea.get(1.0, END).strip() == "":
            mb.showerror("Добавить чек", "Чек пустой!")
            return add_window.focus_set()
        for i in range(0, len(goods_list)):
            db.minus_count(volume_list[i], goods_list[i]+1)
        today = datetime.datetime.today()
        today = today.strftime("%Y-%m-%d-%H.%M.%S")
        db.add_cheque(textarea.get(1.0, END), today, total)
        total = 0
        goods_list = []
        volume_list = []
        table_cheques()
        table.yview_moveto(1)
        add_window.destroy()

    btn_add = Button(
        add_window, text="Добавить позицию",
        command=add_row)
    btn_add.grid(row=5, column=0)

    btn_finish = Button(
        add_window, text="Сохранить чек",
        width=20, command=new_cheque)
    btn_finish.grid(row=6, column=1, pady=10, sticky=W)

    btn_cancel = Button(
        add_window, text="Отмена",
        command=close_add_cheque)
    btn_cancel.grid(row=6, column=1, sticky=E)


# окно обновления товара
def edit_good():
    try:
        print("Изменить товар: " + table.set(table.selection()[0], '#2'))
    except IndexError:
        return print("Товар не выбран!")
    item_id = table.set(table.selection()[0], '#1')
    item = table.selection()[0]
    edit_window = Toplevel()
    edit_window.geometry("300x300")
    edit_window.resizable(False, False)
    edit_window.iconbitmap("icon.ico")
    edit_window.title("Изменить товар")
    edit_window.resizable(0, 0)

    lbl_name = Label(edit_window, text="Наименование:")
    lbl_name.grid(row=0, column=0, padx=20, pady=10, sticky=W)

    lbl_category = Label(edit_window, text="Категория:")
    lbl_category.grid(row=1, column=0, padx=20, pady=10, sticky=W)

    lbl_producer = Label(edit_window, text="Поставщик:")
    lbl_producer.grid(row=2, column=0, padx=20, pady=10, sticky=W)

    lbl_volume = Label(edit_window, text="Количество:")
    lbl_volume.grid(row=3, column=0, padx=20, pady=10, sticky=W)

    lbl_price = Label(edit_window, text="Цена:")
    lbl_price.grid(row=4, column=0, padx=20, pady=10, sticky=W)

    ent_name = Entry(edit_window, width=25)
    ent_name.grid(row=0, column=1)
    ent_name.insert(0, table.set(item, '#2'))
    ent_name.focus_set()

    category = StringVar(
        edit_window)  # переменная для хранения выбора категории
    categories_temp = db.select_categories()  # берем данные из бд
    categories = []  # создаем список категорий

    # заполняем список категорий
    for i in categories_temp:
        categories.append(i[1])
    categories.sort()

    opt_category = OptionMenu(edit_window, category, *categories)
    opt_category.grid(row=1, column=1)
    category.set(table.set(item, '#3'))  # выбрали категорию по умолчанию

    producer = StringVar(
        edit_window)  # переменная для хранения выбора категории
    producers_temp = db.select_producers()  # берем данные из бд
    producers = []  # создаем список категорий

    # заполняем список поставщиков
    for i in producers_temp:
        producers.append(i[1])
    producers.sort()

    opt_producer = OptionMenu(
        edit_window, producer,
        *producers)
    opt_producer.grid(row=2, column=1)
    producer.set(table.set(item, '#4'))  # выбрали поставщика по умолчанию

    ent_volume = Entry(
        edit_window, width=25)
    ent_volume.grid(row=3, column=1)
    ent_volume.insert(0, table.set(item, '#5'))

    ent_price = Entry(
        edit_window, width=25)
    ent_price.grid(row=4, column=1)
    ent_price.insert(
        0, table.set(item, '#6'))

    # подтверждаем обновление товара
    def ok_click():
        if ent_name.get() == "":
            mb.showerror("Изменить товар", "Введите наименование товара!")
            return ent_name.focus_set()
        if ent_volume.get() == "":
            mb.showerror("Изменить товар", "Введите количество товара!")
            return ent_volume.focus_set()
        if ent_price.get() == "":
            mb.showerror("Изменить товар", "Введите цену товара!")
            return ent_price.focus_set()
        try:
            db.edit_good(
                ent_name.get(), category.get(),
                producer.get(), int(ent_volume.get()),
                int(ent_price.get()), item_id)
        except ValueError:
            mb.showerror(
                "Изменить товар",
                """Ввод количества и цены товара\n
осуществляется в числовом формате!""")
            return edit_window.focus_set()
        table_goods()
        select_item(item_id)
        edit_window.destroy()

    btn_ok = Button(
        edit_window, text="Изменить",
        width=10, command=ok_click)
    btn_ok.grid(row=5, column=0, pady=45, padx=5)

    btn_cancel = Button(
        edit_window, text="Отмена",
        width=10, command=edit_window.destroy)
    btn_cancel.grid(row=5, column=1, pady=45, padx=5)


# окно обновления категории
def edit_category():
    try:
        print("Изменить категорию: " + table.set(table.selection()[0], '#2'))
    except IndexError:
        return print("Категория не выбрана!")
    item_id = table.set(table.selection()[0], '#1')
    item = table.selection()[0]
    edit_window = Toplevel()
    edit_window.geometry("300x100")
    edit_window.resizable(False, False)
    edit_window.iconbitmap("icon.ico")
    edit_window.title("Изменить категорию")
    edit_window.resizable(0, 0)

    lbl_category = Label(
        edit_window, text="Категория:")
    lbl_category.grid(row=0, column=0, padx=20, pady=10, sticky=W)

    ent_category = Entry(
        edit_window, width=25)
    ent_category.grid(row=0, column=1)
    ent_category.insert(0, table.set(item, '#2'))
    ent_category.focus_set()

    # подтверждаем имя категории
    def ok_click():
        if ent_category.get() == "":
            mb.showerror(
                "Изменить категорию",
                "Введите имя категории!")
            return ent_category.focus_set()
        db.edit_category(
            ent_category.get(), table.set(item, '#1'))
        table_categories()
        select_item(item_id)
        edit_window.destroy()

    btn_ok = Button(
        edit_window, text="Изменить",
        width=10, command=ok_click)
    btn_ok.grid(row=5, column=0, pady=20, padx=5)

    btn_cancel = Button(
        edit_window, text="Отмена",
        width=10, command=edit_window.destroy)
    btn_cancel.grid(row=5, column=1, pady=20, padx=5)


# окно обновления поставщика
def edit_producer():
    try:
        print("Изменить поставщика: " + table.set(table.selection()[0], '#2'))
    except IndexError:
        return print("Поставщик не выбран!")
    item_id = table.set(table.selection()[0], '#1')
    item = table.selection()[0]
    edit_window = Toplevel()
    edit_window.geometry("300x100")
    edit_window.resizable(False, False)
    edit_window.iconbitmap("icon.ico")
    edit_window.title("Изменить поставщика")
    edit_window.resizable(0, 0)

    lbl_producer = Label(
        edit_window, text="Поставщик:")
    lbl_producer.grid(row=0, column=0, padx=20, pady=10, sticky=W)

    ent_producer = Entry(
        edit_window, width=25)
    ent_producer.grid(row=0, column=1)
    ent_producer.insert(0, table.set(item, '#2'))
    ent_producer.focus_set()

    # подтверждаем имя поставщика
    def ok_click():
        if ent_producer.get() == "":
            mb.showerror(
                "Изменить поставщика",
                "Введите имя поставщика!")
            return ent_producer.focus_set()
        db.edit_producer(
            ent_producer.get(),
            table.set(item, '#1'))
        table_producers()
        select_item(item_id)
        edit_window.destroy()

    btn_ok = Button(
        edit_window, text="Изменить",
        width=10, command=ok_click)
    btn_ok.grid(row=5, column=0, pady=20, padx=5)

    btn_cancel = Button(
        edit_window, text="Отмена",
        width=10, command=edit_window.destroy)
    btn_cancel.grid(row=5, column=1, pady=20, padx=5)


# подтверждение удаления товара
def del_good():
    try:
        print("Удаление товара: " + table.set(table.selection()[0], '#2'))
    except IndexError:
        return print("Товар не выбран!")
    rows = [table.item(x)['values'] for x in table.selection()]
    if len(rows) > 1:
        result = mb.askokcancel(
            "Удалить товары?",
            "Вы действительно хотите удалить выделенные товары?")
    else:
        result = mb.askokcancel(
            "Удалить товар?",
            "Вы действительно хотите удалить товар?")
    if result:
        for row in rows:
            db.del_good(row[0])
        table_goods()


# подтверждение удаления категории
def del_category():
    try:
        print("Удаление категории: " + table.set(table.selection()[0], '#2'))
    except IndexError:
        return print("Категория не выбрана!")
    rows = [table.item(x)['values'] for x in table.selection()]
    if len(rows) > 1:
        result = mb.askokcancel(
            "Удалить категории?",
            "Вы действительно хотите удалить выделенные категории?")
    else:
        result = mb.askokcancel(
            "Удалить категорию?",
            "Вы действительно хотите удалить категорию?")
    if result:
        for row in rows:
            db.del_category(row[0])
        table_categories()


# подтверждение удаления поставщика
def del_producer():
    try:
        print("Удаление поставщика: " + table.set(table.selection()[0], '#2'))
    except IndexError:
        return print("Поставщик не выбран!")
    rows = [table.item(x)['values'] for x in table.selection()]
    if len(rows) > 1:
        result = mb.askokcancel(
            "Удалить поставщиков?",
            "Вы действительно хотите удалить выделенных поставщиков?")
    else:
        result = mb.askokcancel(
            "Удалить поставщика?",
            "Вы действительно хотите удалить поставщика?")
    if result:
        for row in rows:
            db.del_producer(row[0])
        table_producers()


# подтверждение удаления чека
def del_cheque():
    try:
        print("Удаление чека: " + table.set(table.selection()[0], '#1'))
    except IndexError:
        return print("Чек не выбран!")
    rows = [table.item(x)['values'] for x in table.selection()]
    if len(rows) > 1:
        result = mb.askokcancel(
            "Удалить чеки?",
            "Вы действительно хотите удалить выделенные чеки?")
    else:
        result = mb.askokcancel(
            "Удалить чек?",
            "Вы действительно хотите удалить чек?")
    if result:
        for row in rows:
            db.del_cheque(row[0])
        table_cheques()


# печатаем чек
def print_cheque():
    try:
        print("Печать чека: " + table.set(table.selection()[0], '#1'))
    except IndexError:
        return print("Чек не выбран!")
    result = mb.askokcancel(
        "Распечатать чек",
        "Распечатать чек?")
    if result:
        try:
            if os.path.isdir("cheques"):
                pass
            else:
                os.mkdir("cheques")
        except Exception:
            mb.showerror("Распечатать чек", "Ошибка при открытии чека!")
        file_path = "cheques\cheque_" + table.set(table.selection(), "#3")
        file_path += ".txt"
        new_file = open(file_path, "w")
        hr = "----------------------------------"
        part1 = hr + "\n    Магазин спортивных товаров\n" + hr
        part1 += "\n     КАССОВЫЙ ЧЕК - *ПРОДАЖА* \n" + hr
        part2 = "\n" + table.set(table.selection(), "#2").rstrip() + "\n" + hr
        part3 = "\nДАТА И ВРЕМЯ: " + table.set(table.selection(), "#3")
        part3 += "\n" + hr
        part4 = "\nИТОГО К ОПЛАТЕ - "
        part4 += str(table.set(table.selection(), "#4") + " руб.")
        part5 = "\n" + hr + "\n       СПАСИБО ЗА ПОКУПКУ!"
        new_file.write(part1)
        new_file.write(part2)
        new_file.write(part3)
        new_file.write(part4)
        new_file.write(part5)
        new_file.close()
        os.startfile(file_path, "print")


# подтверждение выхода из программы
def exit():
    result = mb.askokcancel("Выход из программы", "Выйти из программы?")
    if result:
        root.destroy()

# переменные для составления чека
total = 0  # итоговая цена чека
goods_list = []  # купленные товары
volume_list = []  # их цены

# настройки главного окна
root = Tk()
root.geometry("1024x600")
root.resizable(False, False)
root.title("Магазин спортивных товаров")
root.iconbitmap("icon.ico")
root.protocol("WM_DELETE_WINDOW", exit)  # обработка выхода из приложения

# виджеты главного окна
lbl_logo = Label(
    text="Магазин спортивных товаров", font="Calibri 54",
    justify=CENTER)
lbl_logo.grid(row=0, column=0, columnspan=3, padx=65, pady=25)

table = ttk.Treeview(columns=("empty"), show='headings', height=12)

btn_goods = Button(
    text="Товары", font="Calibri 18",
    width=12, command=table_goods)
btn_goods.grid(row=1, column=0, sticky=E, padx=15, pady=12)

btn_categories = Button(
    text="Категории", font="Calibri 18",
    width=12, command=table_categories)
btn_categories.grid(row=2, column=0, sticky=E, padx=15)

btn_producers = Button(
    text="Поставщики", font="Calibri 18",
    width=12, command=table_producers)
btn_producers.grid(row=3, column=0, sticky=E, padx=15, pady=12)

btn_cheques = Button(
    text="Чеки", font="Calibri 18",
    width=12, command=table_cheques)
btn_cheques.grid(row=4, column=0, sticky=E, padx=15)

btn_exit = Button(
    text="Выход", font="Calibri 18",
    width=12, command=exit)
btn_exit.grid(row=5, column=0, sticky=E, padx=15, pady=12)

# по умолчанию запускаем таблицу Товары
table_goods()

root.mainloop()
