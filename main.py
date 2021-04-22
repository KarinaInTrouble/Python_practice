import sqlite3
import pandas as pd


while True:
    print("""\nВыберите задание, которое необходимо выполнить:
    1 - Вывести таблицы базы данных
    2 - Вывести наименования всех стран, которые начинаются с буквы А
    3 - Вывести наименования улиц, которые встречаются в 5 и более городах
    4 - Вывести наименования улиц для страны Российская Федерация
    5 - Выход из программы\n""")
    choice = int(input(">> "))
    if choice == 1:
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        df_1 = pd.read_sql("SELECT * FROM City", con) #df - dataframe pandas
        print("Таблица City\n", df_1, "\n")
        df_2 = pd.read_sql("SELECT * FROM Country", con)
        print("Таблица Country\n", df_2, "\n")
        df_3 = pd.read_sql("SELECT * FROM Street", con)
        print("Таблица Street\n", df_3, "\n")

    
    elif choice == 2:
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        df = pd.read_sql("""
        SELECT * FROM Country
        WHERE country_name LIKE 'А%';
        """, con)
        print("\n", df, "\n")
        continue


    elif choice == 3:

        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        df = pd.read_sql("""
        SELECT street_name, count(*) as count_street
        FROM Street JOIN City ON (Street.city_id = City.id)
        GROUP BY street_name
        HAVING count_street >= 5;
        """, con)
        print("\n", df, "\n")
        continue
    
    elif choice == 4:
        con = sqlite3.connect('mydatabase.db')
        cursorObj = con.cursor()
        df = pd.read_sql("""
        SELECT street_name FROM Street JOIN City ON (Street.city_id = City.id)
        WHERE country_id = 1
        GROUP BY street_name;
        """, con)
        print("\n", df, "\n")
        continue

    elif choice == 5:
        print ("Программа завершила работу! ")
        break
