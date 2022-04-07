import unittest

from task_09_word_analysis_2.main import check_palindrome


class Test09CheckPalindrome(unittest.TestCase):
    def test_check_palindrome_madam(self):
        """
        Проверяем обычный кейс. При вводе "мадам" True
        """
        is_palindrome = check_palindrome("мадам")
        self.assertEqual(is_palindrome, True)

    def test_check_palindrome_abccba(self):
        """
        Проверяем обычный кейс. При вводе "abccba" должны получить True
        """
        is_palindrome = check_palindrome("abccba")
        self.assertEqual(is_palindrome, True)

    def test_check_palindromen_abbd(self):
        """
        Проверяем обычный кейс. При вводе "abbd" должны получить False
        """
        is_palindrome = check_palindrome("abbd")
        self.assertEqual(is_palindrome, False)


if __name__ == '__main__':
    unittest.main()
