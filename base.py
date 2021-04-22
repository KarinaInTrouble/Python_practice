import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def City(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE City(id integer PRIMARY KEY, city_name text, country_id integer, FOREIGN KEY (country_id) REFERENCES Country(id) )")
    con.commit()

def Country(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE Country(id integer PRIMARY KEY, country_name text)")
    con.commit()

def Street(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE Street(id integer PRIMARY KEY, street_name text, city_id integer,FOREIGN KEY (city_id) REFERENCES City(id))")
    con.commit()


con = sql_connection()
Country(con)
City(con)
Street(con)