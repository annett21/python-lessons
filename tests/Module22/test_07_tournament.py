from pathlib import Path

import pytest
from pytest import TempPathFactory

from Module22.task_07_tournament.main import (
    extract_participants,
    extract_passing_score,
    read_file,
    write_file,
    filter_participants_by_score,
    sort_participants_by_score,
    prepare_to_write,
)


@pytest.fixture
def temp_file(tmp_path_factory: TempPathFactory) -> Path:
    tmp_dir = tmp_path_factory.mktemp("temp_dir")
    tmp_file = tmp_dir / "temp_file.txt"
    tmp_file.touch()
    return tmp_file


class TestReadFile:
    def test_read_empty_file(self, temp_file: Path):
        expected_data = ""

        data = read_file(temp_file.absolute())

        assert expected_data == data

    def test_read_file(self, temp_file: Path):
        expected_data = "My name is Denis."
        temp_file.write_text(expected_data)

        data = read_file(temp_file.absolute())

        assert expected_data == data


class TestWriteFile:
    def test_write_to_unexisted_file(self, temp_file: Path):
        file_path = temp_file.parent / "unexisted_file.txt"
        expected_data = "My name is Denis."

        assert not file_path.exists()
        write_file(file_path.absolute(), expected_data)
        assert file_path.exists()

        assert expected_data == file_path.read_text()

    def test_write_to_empty_file(self, temp_file: Path):
        expected_data = "My name is Denis."

        write_file(temp_file.absolute(), expected_data)

        assert expected_data == temp_file.read_text()

    def test_overwrite_file(self, temp_file: Path):
        expected_data = "My name is Denis."
        temp_file.write_text("Another text")

        write_file(temp_file.absolute(), expected_data)

        assert expected_data == temp_file.read_text()


class TestExtractPassingScore:
    def test_empty_text(self):
        empty_text = ""

        with pytest.raises(ValueError):
            extract_passing_score(empty_text)

    def test_invalid_text(self):
        invalid_text = "haha\nbugaga\n12"

        with pytest.raises(ValueError):
            extract_passing_score(invalid_text)

    def test_valid_text(self):
        valid_text = "22\nqwerty\nasdfgh"

        passing_score = extract_passing_score(valid_text)

        assert 22 == passing_score


class TestExtractParticipants:
    def test_valid_text(self):
        valid_text = (
            "80\n"
            "Ivanov Serg 80\n"
            "Sergeev Petr 92\n"
            "Petrov Vasiliy 98\n"
            "Vasiliev Maxim 78"
        )
        expected_data = [
            ("Ivanov", "Serg", 80),
            ("Sergeev", "Petr", 92),
            ("Petrov", "Vasiliy", 98),
            ("Vasiliev", "Maxim", 78),
        ]

        participants = extract_participants(valid_text)

        assert expected_data == participants


class TestFilterParticipantsByScore:
    def test_filter_gt_80(self):
        participants = [
            ("Ivanov", "Serg", 80),
            ("Sergeev", "Petr", 92),
            ("Petrov", "Vasiliy", 98),
            ("Vasiliev", "Maxim", 78),
        ]
        expected_data = [("Sergeev", "Petr", 92), ("Petrov", "Vasiliy", 98)]

        filtered_participants = filter_participants_by_score(participants, 80)

        assert filtered_participants == expected_data


class TestSortParticipantByScore:
    def test_sort_by_score(self):
        participants = [
            ("Ivanov", "Serg", 80),
            ("Sergeev", "Petr", 92),
            ("Petrov", "Vasiliy", 98),
            ("Vasiliev", "Maxim", 78),
        ]
        expected_data = [
            ("Petrov", "Vasiliy", 98),
            ("Sergeev", "Petr", 92),
            ("Ivanov", "Serg", 80),
            ("Vasiliev", "Maxim", 78),
        ]

        sorted_participants = sort_participants_by_score(participants)

        assert sorted_participants == expected_data


class TestPrepareToWrite:
    def test_prepare_to_write(self):
        participants = [
            ("Petrov", "Vasiliy", 98),
            ("Sergeev", "Petr", 92),
            ("Ivanov", "Serg", 80),
            ("Vasiliev", "Maxim", 78),
        ]
        expected_data = (
            "4\n"
            "1) V. Petrov 98\n"
            "2) P. Sergeev 92\n"
            "3) S. Ivanov 80\n"
            "4) M. Vasiliev 78"
        )

        prepared_data = prepare_to_write(participants)

        assert prepared_data == expected_data
