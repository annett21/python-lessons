from unittest import TestCase
from unittest.mock import mock_open, patch

from Module22.task_02_zen_of_python.main import read_file, reverse_lines


class TestTask02(TestCase):
    def test_read_file(self):
        path_file = "path/to/some/file"
        read_data = "42 ha-ha"

        mo = mock_open(read_data=read_data)
        with patch("builtins.open", mo):
            result = read_file(path_file)

        mo.assert_called_once_with(path_file, "r")
        self.assertEqual(read_data, result)

    def test_reverse_lines(self):
        lines = "a\nb\nc\nd"
        reversed_lines = reverse_lines(lines)
        self.assertEqual("d\nc\nb\na", reversed_lines)

    def test_reverse_lines_empty_str(self):
        lines = ""
        reversed_lines = reverse_lines(lines)
        self.assertEqual("", reversed_lines)

    def test_reverse_lines_one_line(self):
        lines = "abcdf"
        reversed_lines = reverse_lines(lines)
        self.assertEquals("abcdf", reversed_lines)
