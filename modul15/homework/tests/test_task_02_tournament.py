import unittest

from task_02_tournament.main import get_participants_names


class Test02GetParticipantsNames(unittest.TestCase):
    def test_get_participants_names(self):
        """
        Проверяем обычный кейс. Выводим элементы списка только с чётными индексами.
        """
        participants_names = get_participants_names(["Артемий", "Борис", "Влад", "Гоша"])
        self.assertEqual(participants_names, ["Артемий", "Влад"])


if __name__ == '__main__':
    unittest.main()
