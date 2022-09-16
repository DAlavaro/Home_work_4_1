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
        actors1 = []
        actors = []
        for i in result:
            k = ', '.join(i).split(', ')
            for j in k:
                if j in actors1 and j not in actors and j != one and j != two:
                    actors.append(j)
                else:
                    actors1.append(j)
        return actors

# print(get_actors('Rose McIver', 'Ben Lamb'))



