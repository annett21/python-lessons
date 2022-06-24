import pytest

from Module22.task_01_nums_sum_2.main import normalize_file_data, read_file, write_file


class TestTask01:
    def test_read_file(self, tmp_path_factory: pytest.TempPathFactory):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_01")
        tmp_file = tmp_dir / "test_file.txt"
        file_data = "     2\n\n2\n  2\n         2"
        tmp_file.write_text(file_data)

        result = read_file(str(tmp_file.absolute()))

        assert result == file_data

    def test_normalize_file_data(self):
        file_data = "     2\n\n2\n  2\n         2"
        result = normalize_file_data(file_data)
        assert [2, 2, 2, 2] == result

    def test_write_file(self, tmp_path_factory: pytest.TempPathFactory):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_01")
        tmp_file = tmp_dir / "test_file.txt"
        text = "some my test text"

        write_file(str(tmp_file.absolute()), text)

        assert tmp_file.read_text() == text
