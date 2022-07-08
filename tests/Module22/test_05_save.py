from pathlib import Path
from unittest.mock import Mock, call

from pytest import TempPathFactory, fixture
from pytest_mock import MockFixture

from Module22.task_05_save.main import input_abs_dir_path, input_file_name, save_file


@fixture
def print_m(mocker: MockFixture):
    return mocker.patch("builtins.print")


@fixture
def input_m(mocker: MockFixture):
    return mocker.patch("builtins.input")


@fixture
def tmp_empty_dir(tmp_path_factory: TempPathFactory):
    return tmp_path_factory.mktemp("tmp_empty_dir")


class TestInputAbsoluteDirectoryPath:
    def test_abs_dir_path(self, tmp_empty_dir: Path, input_m: Mock, print_m: Mock):
        real_path = str(tmp_empty_dir.absolute()).replace("/", " ").strip()
        input_m.side_effect = [
            "unexistent absolute path 1",
            "unexistent absolute path 2",
            real_path,
        ]
        expected_input_call = call(
            "Where would you like to save the document? "
            "Enter the sequence of folders (separated by a space): "
        )
        expected_print_call = call("This path is not exists!")

        dir_path = input_abs_dir_path()

        input_m.assert_has_calls(
            [expected_input_call, expected_input_call, expected_input_call]
        )
        print_m.assert_has_calls([expected_print_call, expected_print_call])

        assert dir_path == str(tmp_empty_dir.absolute())


class TestInputFileName:
    def test_input_unexistent_file_name(self, tmp_empty_dir: Path, input_m: Mock):
        abs_dir_path = str(tmp_empty_dir.absolute())
        file_name = "some_file_name"
        input_m.return_value = file_name

        expected_input_call = call("Enter a file name: ")
        expected_file_path = abs_dir_path + "/" + file_name + ".txt"
        expected_file_existanse = False

        file_path, file_is_exists = input_file_name(abs_dir_path)

        input_m.assert_has_calls((expected_input_call,))

        assert file_path == expected_file_path
        assert file_is_exists == expected_file_existanse

    def test_input_existent_file_name(self, tmp_empty_dir: Path, input_m: Mock):
        abs_dir_path = str(tmp_empty_dir.absolute())
        file_name = "some_file_name"
        tmp_file = tmp_empty_dir / "some_file_name.txt"
        tmp_file.touch()
        abs_file_path = str(tmp_file.absolute())
        input_m.side_effect = (file_name, "no", file_name, "yes")

        expected_input_calls = (
            call("Enter a file name: "),
            call("Do you want to overwrite this file? (yes/no) "),
            call("Enter a file name: "),
            call("Do you want to overwrite this file? (yes/no) "),
        )
        expected_file_path = abs_file_path
        expected_file_existanse = True

        file_path, file_is_exists = input_file_name(abs_dir_path)

        input_m.assert_has_calls(expected_input_calls, any_order=False)

        assert file_path == expected_file_path
        assert file_is_exists == expected_file_existanse


class TestSaveFile:
    def test_save_unexisted_file(self, tmp_empty_dir: Path):
        text = "some my test text"
        tmp_file = tmp_empty_dir / "some_file_name.txt"

        save_file(str(tmp_file.absolute()), text)

        assert tmp_file.exists()
        assert tmp_file.read_text() == text

    def test_overwrite_existed_file(self, tmp_empty_dir: Path):
        old_text = "some old test text"
        new_text = "bugaga"
        tmp_file = tmp_empty_dir / "test_file.txt"
        tmp_file.write_text(old_text)

        save_file(str(tmp_file.absolute()), new_text)

        assert tmp_file.read_text() == new_text
