import sqlite3
import json


def get_title(name):
    """
    Поиск по названию
    """
    with sqlite3.connect("netflix.db") as tab:
        cursor = tab.cursor()
        sqlite_query = f"""
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title = '{name}' 
        ORDER BY release_year desc limit 1
        """
        cursor.execute(sqlite_query)
        result = cursor.fetchall()
        result = {'title': result[0][0],
                  'country': result[0][1],
                  'release_year': result[0][2],
                  'genre': result[0][3],
                  'description': result[0][4]
                  }
        return result


def get_film_year(one, two):
    """
    Поиск по диапазону лет выпуска.
    """
    with sqlite3.connect("netflix.db") as tab:
        cursor = tab.cursor()
        sqlite_query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {one} and {two}
            """
        cursor.execute(sqlite_query)
        result = cursor.fetchall()

        table = []
        for i in result:
            book = {'title': i[0], 'release_year': i[1]}
            table.append(book)

        return table


def get_rating(type):
    """
    Поиск по рейтингу.
    """
    if type == 'children':
        rate1, rate2, rate3 = 'G', 'Q', 'Q'
    elif type == 'adult':
        rate1, rate2, rate3 = 'R', 'NC-17', 'Q'
    elif type == 'family':
        rate1, rate2, rate3 = 'G', 'PG', 'PG-13'
    with sqlite3.connect("netflix.db") as tab:
        cursor = tab.cursor()
        sqlite_query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating = '{rate1}'
            OR rating = '{rate2}'
            OR rating = '{rate3}'
            """
        cursor.execute(sqlite_query)
        result = cursor.fetchall()
        table = []
        for i in result:
            line = {'title': i[0], 'rating': i[1], 'description': i[2]}
            table.append(line)
        return table


def get_genre(style):
    with sqlite3.connect("netflix.db") as tab:
        cursor = tab.cursor()
        sqlite_query = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{style}%'
            ORDER BY release_year desc limit 10
            """
        cursor.execute(sqlite_query)
        result = cursor.fetchall()
        table = []
        for i in result:
            line = {'title': i[0], 'description': i[1]}
            table.append(line)

        return table

# print(get_title('A Billion Colour Story'))
# print(get_rating('family'))
# print(get_genre('horror'))
