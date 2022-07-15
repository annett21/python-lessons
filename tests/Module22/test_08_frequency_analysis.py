from pathlib import Path

import pytest
from pytest import TempPathFactory

from Module22.task_08_frequency_analysis.main import (
    read_file,
    write_file,
    get_all_letters,
    analyse_letters,
    sort_stats,
    make_pretty_stats,
)


@pytest.fixture
def temp_file(tmp_path_factory: TempPathFactory) -> Path:
    tmp_dir = tmp_path_factory.mktemp("temp_dir")
    tmp_file = tmp_dir / "temp_file.txt"
    tmp_file.touch()
    return tmp_file


class TestReadFile:
    def test_empty_file(self, temp_file: Path):
        expected_data = ""

        data = read_file(temp_file.absolute())

        assert expected_data == data

    def test_non_empty_file(self, temp_file: Path):
        expected_data = "My name is Denis."
        temp_file.write_text(expected_data)

        data = read_file(temp_file.absolute())

        assert expected_data == data


class TestWriteFile:
    def test_unexisted_file(self, temp_file: Path):
        file_path = temp_file.parent / "unexisted_file.txt"
        expected_data = "My name is Denis."

        assert not file_path.exists()
        write_file(file_path.absolute(), expected_data)
        assert file_path.exists()

        assert expected_data == file_path.read_text()

    def test_empty_file(self, temp_file: Path):
        expected_data = "My name is Denis."

        write_file(temp_file.absolute(), expected_data)

        assert expected_data == temp_file.read_text()

    def test_existed_file(self, temp_file: Path):
        expected_data = "My name is Denis."
        temp_file.write_text("Another text")

        write_file(temp_file.absolute(), expected_data)

        assert expected_data == temp_file.read_text()


class TestGetAllLetters:
    def test_valid_letters(self):
        test_text = "QQQSSSfffkkk"
        expected_data = "qqqsssfffkkk"

        letters = get_all_letters(test_text)

        assert letters == expected_data

    def test_with_punctuation_marks(self):
        test_text = "QQQ,SSS;fff#kkk.ggg!"
        expected_data = "qqqsssfffkkkggg"

        letters = get_all_letters(test_text)

        assert letters == expected_data

    def test_with_numbers(self):
        test_text = "QQQSSSfffkkk123ggg"
        expected_data = "qqqsssfffkkkggg"

        letters = get_all_letters(test_text)

        assert letters == expected_data

    def test_with_russian_letters(self):
        test_text = "QQQSSSfffkkkФЫВАggg"
        expected_data = "qqqsssfffkkkggg"

        letters = get_all_letters(test_text)

        assert letters == expected_data


class TestAnalyzeLetters:
    def test_valid_letters(self):
        test_letters = "qwertyqweasdasdasd"
        expected_result = {
            "q": 0.111,
            "w": 0.111,
            "e": 0.111,
            "r": 0.056,
            "t": 0.056,
            "y": 0.056,
            "a": 0.167,
            "s": 0.167,
            "d": 0.167,
        }

        result = analyse_letters(test_letters)

        assert result == expected_result

    def test_empty_string(self):
        test_letters = ""
        expected_data = {}

        result = analyse_letters(test_letters)

        assert result == expected_data


class TestSortStats:
    def test_valid_data(self):
        test_stats = {
            "a": 0.167,
            "r": 0.056,
            "q": 0.111,
            "w": 0.111,
            "s": 0.167,
            "y": 0.056,
            "e": 0.111,
            "d": 0.167,
            "t": 0.056,
        }
        expected_result = [
            ("a", 0.167),
            ("d", 0.167),
            ("s", 0.167),
            ("e", 0.111),
            ("q", 0.111),
            ("w", 0.111),
            ("r", 0.056),
            ("t", 0.056),
            ("y", 0.056),
        ]

        result = sort_stats(test_stats)

        assert result == expected_result


class TestMakePrettyStats:
    def test_valid_stats(self):
        test_stats = [
            ("a", 0.167),
            ("d", 0.167),
            ("s", 0.167),
            ("e", 0.111),
            ("q", 0.111),
            ("w", 0.111),
            ("r", 0.056),
            ("t", 0.056),
        ]
        expected_result = (
            "a 0.167\nd 0.167\ns 0.167\ne 0.111\nq 0.111\nw 0.111\nr 0.056\nt 0.056"
        )

        result = make_pretty_stats(test_stats)

        assert result == expected_result
