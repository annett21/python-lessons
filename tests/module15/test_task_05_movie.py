import unittest

from modul15.homework.task_05_movie.main import add_favorite_film


class Test05AddFavoriteFilm(unittest.TestCase):
    def test_add_favorite_film(self):
        """
        Проверяем обычный кейс.
        При вводе ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
        должны получить (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
        """
        available_movies = [
            "Крепкий орешек",
            "Назад в будущее",
            "Таксист",
            "Леон",
            "Богемская рапсодия",
            "Город грехов",
            "Мементо",
            "Отступники",
            "Деревня",
        ]
        new_favorite_movies = ["Леон", "Безумный Макс", "Мементо", "Царь горы"]

        favorite_movies, unavailable_movies = add_favorite_film(
            new_favorite_movies, available_movies
        )

        self.assertSetEqual(set(favorite_movies), set(["Леон", "Мементо"]))
        self.assertSetEqual(set(unavailable_movies), set(["Безумный Макс", "Царь горы"]))


if __name__ == "__main__":
    unittest.main()
