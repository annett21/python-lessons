from unittest import TestCase
from unittest.mock import mock_open, patch

from Module22.task_01_nums_sum_2.main import normalize_file_data, read_file, write_file


class TestTask01(TestCase):
    def test_read_file(self):
        file_path = "some/file/path"
        read_data = "     2\n\n2\n  2\n         2"

        with patch("builtins.open", mock_open(read_data=read_data)) as m:
            result = read_file(file_path)

        m.assert_called_once_with(file_path, "r")
        self.assertEqual(result, read_data)

    def test_normalize_file_data(self):
        file_data = "     2\n\n2\n  2\n         2"
        result = normalize_file_data(file_data)
        self.assertEqual([2,2,2,2], result)

    def test_write_file(self):
        file_path = "some/path/to/file"
        text = "abracadabra"

        mo = mock_open()
        with patch("builtins.open", mo):
            write_file(file_path, text)

        mo.assert_called_once_with(file_path, "w")
        handle = mo()
        handle.write.assert_called_once_with(text)
