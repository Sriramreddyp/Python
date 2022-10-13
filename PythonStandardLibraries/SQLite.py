import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("Movies.json").read_text())
# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    # for movie in movies:
    cursor = conn.execute(command)
    # conn.commit()
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
