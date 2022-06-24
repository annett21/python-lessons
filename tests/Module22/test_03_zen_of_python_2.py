import pytest

from Module22.task_03_zen_of_python_2.main import (
    count_letters,
    count_lines,
    count_words,
    find_most_rare_letter,
    read_file,
)


class TestTask03:
    def test_read_file(self, tmp_path_factory: pytest.TempPathFactory):
        tmp_dir = tmp_path_factory.mktemp("temp_dir_task_01")
        tmp_file = tmp_dir / "test_file.txt"
        file_data = "ohohohoho mama mia"
        tmp_file.write_text(file_data)

        result = read_file(str(tmp_file.absolute()))

        assert result == file_data

    def test_count_letters(self):
        text = "qwertyasdfg"
        letters_quantity = count_letters(text)
        assert 11 == letters_quantity

    def test_count_letters_with_punctuation_marks_and_witespaces(self):
        text = "Hello, World!\n\tMy name is Denis :)"
        letters_quantity = count_letters(text)
        assert 23 == letters_quantity

    def test_count_words(self):
        text = "word word word"
        words_quantity = count_words(text)
        assert 3 == words_quantity

    def test_count_words_in_many_lines(self):
        text = "word word\nword"
        words_quantity = count_words(text)
        assert 3 == words_quantity

    def test_count_words_with_nonnalpha_symbols(self):
        text = "word word\n Hello, world :)"
        words_quantity = count_words(text)
        assert 4 == words_quantity

    def test_count_words_with_nonalpha_symbols_inside_words(self):
        text = "Hello, I'm Den! You're able to choose yes/no, he-he)"
        words_quantity = count_words(text)
        assert 9 == words_quantity

    def test_count_lines(self):
        text = "Hello, Anna)"
        lines_quantity = count_lines(text)
        assert 1 == lines_quantity

    def test_count_lines_multilines_text(self):
        text = "Hello, Anna)\n\nHa\nabracadabra\n"
        lines_quantity = count_lines(text)
        assert 5 == lines_quantity

    def test_find_most_rare_letter(self):
        text = "aaabbbbcccdffgg"
        most_rare_letter = find_most_rare_letter(text)
        assert "d" == most_rare_letter

    def test_find_most_rare_letter_with_nonalpha_symbols(self):
        text = "a'aabb-bbcc cdffgg)"
        most_rare_letter = find_most_rare_letter(text)
        assert "d" == most_rare_letter

    def test_find_most_rare_letter_many_variants(self):
        text = "a'aabb-bbcc cDffgghH yyy zz)"
        most_rare_letter = find_most_rare_letter(text)
        assert "d" == most_rare_letter

    def test_find_most_rare_letter_with_upper_letters(self):
        text = "a'aabb-bbcc cdffggh yyy zz)"
        most_rare_letter = find_most_rare_letter(text)
        assert "h" == most_rare_letter
