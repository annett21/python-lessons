import unittest

from task_08_running_nums.main import shift_list


class Test08ShiftList(unittest.TestCase):
    def test_shift_list_1_step(self):
        """
        Проверяем обычный кейс. При вводе 1, [1, 2, 3, 4, 5] должны получить  [5, 1, 2, 3, 4]
        """
        print_result = shift_list(1, [1, 2, 3, 4, 5])
        self.assertEqual(print_result, [5, 1, 2, 3, 4])

    def test_shift_list_3_step(self):
        """
        Проверяем обычный кейс. При вводе 3, [1, 4, -3, 0, 10] должны получить [-3, 0, 10, 1, 4]
        """
        print_result = shift_list(3, [1, 4, -3, 0, 10])
        self.assertEqual(print_result, [-3, 0, 10, 1, 4])


if __name__ == '__main__':
    unittest.main()
