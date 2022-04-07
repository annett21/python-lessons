import unittest

from task_07_containers.main import search_serial_number_new_container


class Test07SearchSerialNumberNewContainer(unittest.TestCase):
    def test_main(self):
        """
        Проверяем обычный кейс. При вводе [165, 163, 160, 160, 157, 157, 155, 154] должны получить 3
        """
        list_container_weights = [165, 163, 160, 160, 157, 157, 155, 154]
        new_container_weight = 162

        serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)

        self.assertEqual(serial_number_new_container, 3)


if __name__ == '__main__':
    unittest.main()
