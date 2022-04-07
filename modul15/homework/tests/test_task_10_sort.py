import unittest

from task_10_sort.main import sort_list


class Test10Sort(unittest.TestCase):
    def test_sort_list(self):
        """
        Проверяем обычный кейс. При вводе [1, 4, -3, 0, 10] должны получить [-3, 0, 1, 4, 10]
        """
        sorted_list = sort_list([1, 4, -3, 0, 10])
        self.assertEqual(sorted_list, [-3, 0, 1, 4, 10])


if __name__ == '__main__':
    unittest.main()
