from unittest import TestCase
from unittest.mock import call, mock_open, patch

from Module22.task_03_zen_of_python_2.main import (
    count_letters,
    count_lines,
    count_words,
    find_most_rare_letter,
    print_report,
    read_file,
)


class TestTask03(TestCase):
    def test_read_file(self):
        file_data = "ohohohoho mama mia"
        file_path = "path/to/my/favorite/file"

        mo = mock_open(read_data=file_data)
        with patch("builtins.open", mo):
            result = read_file(file_path)

        mo.assert_called_once_with(file_path, "r")
        self.assertEqual(file_data, result)

    def test_count_letters(self):
        text = "qwertyasdfg"
        letters_quantity = count_letters(text)
        self.assertEqual(11, letters_quantity)

    def test_count_letters_with_punctuation_marks_and_witespaces(self):
        text = "Hello, World!\n\tMy name is Denis :)"
        letters_quantity = count_letters(text)
        self.assertEqual(23, letters_quantity)

    def test_count_words(self):
        text = "word word word"
        words_quantity = count_words(text)
        self.assertEqual(3, words_quantity)

    def test_count_words_in_many_lines(self):
        text = "word word\nword"
        words_quantity = count_words(text)
        self.assertEqual(3, words_quantity)

    def test_count_words_with_nonnalpha_symbols(self):
        text = "word word\n Hello, world :)"
        words_quantity = count_words(text)
        self.assertEqual(4, words_quantity)

    def test_count_words_with_nonalpha_symbols_inside_words(self):
        text = "Hello, I'm Den! You're able to choose yes/no, he-he)"
        words_quantity = count_words(text)
        self.assertEqual(9, words_quantity)

    def test_count_lines(self):
        text = "Hello, Anna)"
        lines_quantity = count_lines(text)
        self.assertEquals(1, lines_quantity)

    def test_count_lines_multilines_text(self):
        text = "Hello, Anna)\n\nHa\nabracadabra\n"
        lines_quantity = count_lines(text)
        self.assertEquals(5, lines_quantity)

    def test_find_most_rare_letter(self):
        text = "aaabbbbcccdffgg"
        most_rare_letter = find_most_rare_letter(text)
        self.assertEquals("d", most_rare_letter)

    def test_find_most_rare_letter_with_nonalpha_symbols(self):
        text = "a'aabb-bbcc cdffgg)"
        most_rare_letter = find_most_rare_letter(text)
        self.assertEquals("d", most_rare_letter)

    def test_find_most_rare_letter_many_variants(self):
        text = "a'aabb-bbcc cDffgghH yyy zz)"
        most_rare_letter = find_most_rare_letter(text)
        self.assertEquals("d", most_rare_letter)

    def test_find_most_rare_letter_with_upper_letters(self):
        text = "a'aabb-bbcc cdffggh yyy zz)"
        most_rare_letter = find_most_rare_letter(text)
        self.assertEquals("h", most_rare_letter)

    @patch("builtins.print")
    def test_print_report(self, mock_print):
        letters_quantity = 1000
        words_quantity = 100
        lines_quantity = 10
        most_rare_letter = "z"

        print_report(letters_quantity, words_quantity, lines_quantity, most_rare_letter)

        expected_calls = [
            call("Количество букв в файле:", letters_quantity),
            call("Количество слов в файле:", words_quantity),
            call("Количество строк в файле:", lines_quantity),
            call("Наиболее редкая буква:", most_rare_letter),
        ]
        mock_print.assert_has_calls(expected_calls)
