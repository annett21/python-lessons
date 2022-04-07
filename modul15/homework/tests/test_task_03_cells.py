import unittest

from task_03_cells.main import select_cells


class Test03SelectCells(unittest.TestCase):
    def test_select_cells(self):
        """
        Проверяем обычный кейс. При параметрах [5, 3, 0, 6, 2, 10, 4]  должны получить [0 2, 4]
        """
        cells = [3, 0, 6, 2, 10, 4]
        res_cells = select_cells(cells)
        self.assertEqual(res_cells, [0, 2, 4])

    def test_select_cells_no_result(self):
        """
        Проверяем обычный кейс. При параметрах [1, 2, 3]  должны получить []
        """
        cells = [1, 2, 3]
        res_cells = select_cells(cells)
        self.assertEqual(res_cells, [])


if __name__ == '__main__':
    unittest.main()
