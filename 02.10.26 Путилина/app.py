from flask import Flask, render_template

app = Flask(__name__)

# Список фильмов
movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre": "Фантастика",
        "description": "Если честно, то я без понятия. Посмотрела 40 минут - мне не зашло))"
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre": "Фантастика, боевик",
        "description": "Это я вообще не смотрела))"
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 8.1,
        "genre": "Мультфильм",
        "description": "Ваще офигенный мульт. Ставлю 10 из 10!"
    },
    {
        "id": 4,
        "title": "Очень странные дела",
        "year": 2016,
        "rating": 8.1,
        "genre": "Ужасы",
        "description": "Вот это топ! Мой любимый сериал! Одиннадцать, демогоргоны и тд и тп))"
    },
    {
        "id": 5,
        "title": "Игра престолов",
        "year": 2011,
        "rating": 9.5,
        "genre": "Драма",
        "description": "Лучший сериал! Так плакала, слишком много смертей и сюжетных поворотов. Ставлю 100 из 100!"
    },
    {
        "id": 6,
        "title": "Малефисента",
        "year": 2014,
        "rating": 8.6,
        "genre": "Фэнтези",
        "description": "Мой любимы мульт! Джоли прекрасна, как и всегда. Я шиперила ее и ворона..."
    }
]


# Главная страница
@app.route("/")
def index():
    return render_template("index.html", movies=movies)


# Страница отдельного фильма
@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie.html", movie=movie)

    return "Фильм не найден. Очень жаль, но у меня добавлено только 6 фильмов. Сори..", 404


# Запуск
if __name__ == "__main__":
    app.run(debug=True)
