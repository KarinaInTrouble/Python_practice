import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()
data_1 = [(1, "Российская Федерация"), (2, "Республика Казахстан"), (3, "Республика Узбекистан"), (4, "Аргентина"), (5, "Афганистан")]
data_2 = [(1, "Архангельск", 1), (2, "Азов", 1), (3, "Брянск", 1), (4, "Москва", 1), (5, "Алматы", 2), (6, "Караганда", 2), (7, "Нур-султан", 2)]
data_3 = [(1, "Ленина", 1), (2, "Ленина", 2), (3, "Ленина", 3), (4, "Ленина" , 4), (5, "Ленина", 6),(6, "Мира", 1),
(7, "Мира", 2), (8, "Мира", 4), (9, "Мира", 5), (10, "Мира", 6), (11, "Центральная", 3), (12, "Центральная", 4), (13, "Мира", 3)]
cursorObj.executemany("INSERT INTO Country VALUES(?, ?)", data_1)
cursorObj.executemany("INSERT INTO City VALUES(?, ?, ?)", data_2)
cursorObj.executemany("INSERT INTO Street VALUES(?, ?, ?)", data_3)


con.commit()