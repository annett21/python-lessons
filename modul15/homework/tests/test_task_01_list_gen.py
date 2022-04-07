import unittest

from task_01_list_gen.main import get_odd_numbers


class Test01GetOddNumbers(unittest.TestCase):
    def test_get_odd_numbers_boundary_conditions(self):
        """
        Проверяем граничные условия. При вводе 1 должна получиться последовательность [1]
        """
        odd_numbers = get_odd_numbers(1)
        self.assertEqual(odd_numbers, [1])

    def test_get_odd_numbers(self):
        """
        Проверяем обычный кейс. При вводе 14 должна получиться последовательность [1, 3, 5, 7, 9, 11, 13]
        """

        odd_numbers = get_odd_numbers(14)
        self.assertEqual(odd_numbers, [1, 3, 5, 7, 9, 11, 13])


if __name__ == '__main__':
    unittest.main()
