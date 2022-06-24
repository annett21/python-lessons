import pytest

from Module22.task_02_zen_of_python.main import read_file, reverse_lines


class TestTask02:
    def test_read_file(self, tmp_path_factory: pytest.TempPathFactory):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_01")
        tmp_file = tmp_dir / "test_file.txt"
        file_data = "42 ha-ha"
        tmp_file.write_text(file_data)

        result = read_file(str(tmp_file.absolute()))

        assert result == file_data

    def test_reverse_lines(self):
        lines = "a\nb\nc\nd"
        reversed_lines = reverse_lines(lines)
        assert "d\nc\nb\na" == reversed_lines

    def test_reverse_lines_empty_str(self):
        lines = ""
        reversed_lines = reverse_lines(lines)
        assert "" == reversed_lines

    def test_reverse_lines_one_line(self):
        lines = "abcdf"
        reversed_lines = reverse_lines(lines)
        assert "abcdf" == reversed_lines
