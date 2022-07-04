import pytest

from Module22.task_04_files_and_folders.main import (
    count_files,
    count_size_kb,
    count_subdirs,
)


class TestTask04CountSizeKb:
    def test_count_size_kb_empty_dir(self, tmp_path_factory: pytest.TempPathFactory):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")  # 64 bytes

        result = count_size_kb(tmp_dir)

        assert result == 0.064

    def test_count_size_kb_dir_with_empty_file(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")  # 64 bytes
        tmp_file = tmp_dir / "temp_file.txt"  # 32 bytes

        tmp_file.write_bytes(b"")  # 0 bytes

        result = count_size_kb(tmp_dir)

        assert result == 0.096

    def test_count_size_kb_dir_with_non_empty_file(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")  # 64 bytes
        tmp_file = tmp_dir / "temp_file.txt"  # 32 bytes

        tmp_file.write_bytes(b"aaaaa\nbbbbb")  # 11 bytes

        result = count_size_kb(tmp_dir)

        assert result == 0.107

    def test_count_size_kb_dir_with_several_files(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")  # 64 bytes
        tmp_file1 = tmp_dir / "temp_file1.txt"  # 32 bytes
        tmp_file2 = tmp_dir / "temp_file2.txt"  # 32 bytes

        tmp_file1.write_bytes(b"Here is 17 bytes.")  # 17 bytes
        tmp_file2.write_bytes(b"And here is 21 bytes.")  # 21 bytes

        result = count_size_kb(tmp_dir)

        assert result == 0.166

    def test_count_size_kb_dir_with_internal_dirs_and_files(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("tema_dir_task_04")  # 64 bytes
        tmp_internal_dir = tmp_dir / "internal_dir"
        tmp_internal_dir.mkdir()  # 96 bytes
        tmp_file1 = tmp_dir / "temp_file1.txt"  # 32 bytes
        tmp_file2 = tmp_internal_dir / "temp_file2.txt"  # 32 bytes
        tmp_file3 = tmp_internal_dir / "temp_file3.txt"  # 32 bytes

        tmp_file1.write_bytes(b"Here is 17 bytes.")  # 17 bytes
        tmp_file2.write_bytes(b"And here is 21 bytes.")  # 21 bytes
        tmp_file3.write_bytes(b"Try guess how many bytes is here)")  # 33 bytes

        result = count_size_kb(tmp_dir)

        assert result == 0.327


class TestTask04CountSubDirs:
    def test_count_subdirs_empty_dir(self, tmp_path_factory: pytest.TempPathFactory):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")

        result = count_subdirs(tmp_dir)

        assert result == 0

    def test_count_subdirs_dir_with_file(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")
        tmp_file = tmp_dir / "temp_file.txt"
        tmp_file.write_bytes(b"")

        result = count_subdirs(tmp_dir)

        assert result == 0

    def test_count_subdirs_dir_with_internal_dir(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")
        tmp_internal_dir = tmp_dir / "internal_dir"
        tmp_internal_dir.mkdir()

        result = count_subdirs(tmp_dir)

        assert result == 1

    def test_count_subdirs_dir_with_many_internal_dirs(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("tema_dir_task_04")
        tmp_internal_dir_1 = tmp_dir / "internal_dir_1"
        tmp_internal_dir_1.mkdir()
        tmp_internal_dir_2 = tmp_dir / "internal_dir_2"
        tmp_internal_dir_2.mkdir()
        tmp_internal_dir_3 = tmp_internal_dir_1 / "internal_dir_3"
        tmp_internal_dir_3.mkdir()
        tmp_internal_dir_4 = tmp_internal_dir_2 / "internal_dir_4"
        tmp_internal_dir_4.mkdir()
        tmp_internal_dir_5 = tmp_internal_dir_2 / "internal_dir_5"
        tmp_internal_dir_5.mkdir()

        result = count_subdirs(tmp_dir)

        assert result == 5


class TestTask04CountFiles:
    def test_count_files_empty_dir(self, tmp_path_factory: pytest.TempPathFactory):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")

        result = count_files(tmp_dir)

        assert result == 0

    def test_count_files_dir_with_one_file(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")
        tmp_file = tmp_dir / "temp_file.txt"
        tmp_file.write_bytes(b"")

        result = count_files(tmp_dir)

        assert result == 1

    def test_count_size_kb_dir_with_two_file(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")
        tmp_file1 = tmp_dir / "temp_file1.txt"
        tmp_file2 = tmp_dir / "temp_file2.txt"
        tmp_file1.write_bytes(b"")
        tmp_file2.write_bytes(b"")

        result = count_files(tmp_dir)

        assert result == 2

    def test_count_files_dir_with_empty_internal_dir(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")
        tmp_internal_dir = tmp_dir / "internal_dir"
        tmp_internal_dir.mkdir()
        tmp_file1 = tmp_dir / "temp_file1.txt"
        tmp_file2 = tmp_dir / "temp_file2.txt"
        tmp_file1.write_bytes(b"")
        tmp_file2.write_bytes(b"")

        result = count_files(tmp_dir)

        assert result == 2

    def test_count_files_dir_with_internal_dirs(
        self, tmp_path_factory: pytest.TempPathFactory
    ):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_04")

        tmp_internal_dir_1 = tmp_dir / "internal_dir_1"
        tmp_internal_dir_1.mkdir()
        tmp_internal_dir_2 = tmp_dir / "internal_dir_2"
        tmp_internal_dir_2.mkdir()
        tmp_internal_dir_3 = tmp_internal_dir_1 / "internal_dir_3"
        tmp_internal_dir_3.mkdir()
        tmp_internal_dir_4 = tmp_internal_dir_2 / "internal_dir_4"
        tmp_internal_dir_4.mkdir()
        tmp_internal_dir_5 = tmp_internal_dir_2 / "internal_dir_5"
        tmp_internal_dir_5.mkdir()

        tmp_file1 = tmp_dir / "temp_file1.txt"
        tmp_file2 = tmp_internal_dir_1 / "temp_file2.txt"
        tmp_file3 = tmp_internal_dir_2 / "temp_file3.txt"
        tmp_file4 = tmp_internal_dir_3 / "temp_file4.txt"
        tmp_file5 = tmp_internal_dir_4 / "temp_file5.txt"
        tmp_file6 = tmp_internal_dir_5 / "temp_file6.txt"
        tmp_file7 = tmp_internal_dir_5 / "temp_file7.txt"
        tmp_file1.write_bytes(b"")
        tmp_file2.write_bytes(b"")
        tmp_file3.write_bytes(b"")
        tmp_file4.write_bytes(b"")
        tmp_file5.write_bytes(b"")
        tmp_file6.write_bytes(b"")
        tmp_file7.write_bytes(b"")

        result = count_files(tmp_dir)

        assert result == 7
