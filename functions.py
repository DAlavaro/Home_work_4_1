import json
import sqlite3


def get_actors(one, two):
    with sqlite3.connect("netflix.db") as tab:
        cursor = tab.cursor()
        sqlite_query = f"""
            SELECT "cast"
            FROM netflix
            WHERE "cast" like '%{one}%'
            AND "cast" like '%{two}%'
            """
        cursor.execute(sqlite_query)
        result = cursor.fetchall()
        # Список для актерев встречающихся 1 раз
        actors1 = []
        # Список для актерев встречающихся 2 раза
        actors2 = []
        # Список для актерев встречающихся более 2 раз
        actors = []
        for i in result:
            # получаем итерируемый список актеров встречающихся в тданном фильме
            k = ', '.join(i).split(', ')
            for j in k:
                # Условие если актер встречается в фильме 2 раза добавить в итоговый список
                if j in actors2 and j not in actors and j != one and j != two:
                    actors.append(j)
                # Условие если актер встречается в фильме 1 раз добавить в список 2
                elif j in actors1 and j not in actors2 and j != one and j != two:
                    actors2.append(j)
                # Есил актер не попал в предыдущие списки и его нет в списке actors1
                # Добавить в список actors1
                elif j not in actors1:
                    actors1.append(j)
        return actors

# print(get_actors('Rose McIver', 'Ben Lamb'))


def search_by_types(type_movie, year, genre):
    """ Получает в качестве аргумента тип картины (фильм или сериал), год выпуска и ее жанр
          Возвращает список названий картин с их описаниями в JSON"""

    with sqlite3.connect('netflix.db') as connection:
        result = connection.cursor()
        sqlite_query = f"""SELECT title, description
                             FROM netflix
                             WHERE type = '{type_movie}'
                              AND release_year = '{year}'
                              AND listed_in LIKE '%{genre}%'
                        """
        result.execute(sqlite_query)
        movies = result.fetchall()
        movie_list = []
        for movie in movies:
            movie_dict = dict()
            movie_dict['title'] = movie[0]
            movie_dict["description"] = movie[1].strip()
            movie_list.append(movie_dict)
        return json.dumps(movie_list)





