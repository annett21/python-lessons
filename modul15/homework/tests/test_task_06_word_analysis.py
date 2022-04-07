import unittest

from task_06_word_analysis.main import count_number_unique_letters


class Test06CountNumberUniqueLetters(unittest.TestCase):
    def test_main_privet(self):
        """
        Проверяем обычный кейс. При вводе "привет"  должны получить "Кол-во уникальных букв: 6"
        """
        number_unique_letters = count_number_unique_letters("привет")

        self.assertEqual(number_unique_letters, 6)

    def test_main_lava(self):
        """
        Проверяем обычный кейс. При вводе "лава"  должны получить "Кол-во уникальных букв: 2"
        """
        number_unique_letters = count_number_unique_letters("лава")

        self.assertEqual(number_unique_letters, 2)


if __name__ == '__main__':
    unittest.main()
