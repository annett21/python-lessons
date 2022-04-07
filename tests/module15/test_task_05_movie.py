import unittest

from task_05_movie.main import add_favorite_movies


class Test05AddFavoriteFilm(unittest.TestCase):
    def test_add_favorite_movies(self):
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

        favorite_movies, unavailable_movies = add_favorite_movies(
            new_favorite_movies, available_movies
        )

        self.assertEqual(favorite_movies, ["Леон", "Мементо"])
        self.assertEqual(unavailable_movies, ["Безумный Макс", "Царь горы"])


if __name__ == "__main__":
    unittest.main()
