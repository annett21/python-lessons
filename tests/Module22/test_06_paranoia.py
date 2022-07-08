import pytest

from Module22.task_06_paranoia.main import (
    encode_file_caesar,
    encode_letter_caesar,
    encode_str_caesar,
)


class TestEncodeCaesar:
    @pytest.mark.parametrize(
        "letter,shift,expected",
        [("a", 1, "b"), ("c", 2, "e"), (" ", 42, " "), ("!", 125, "!"), ("H", 45, "A")],
    )
    def test_encode_letter_caesar(self, letter, shift, expected):
        assert encode_letter_caesar(letter, shift) == expected

    @pytest.mark.parametrize(
        "text,shift,expected",
        [
            ("Hello", 1, "Ifmmp"),
            ("Hello", 2, "Jgnnq"),
            ("Hello", 42, "Xubbe"),
            ("Hello, World!", 125, "Czggj, Rjmgy!"),
        ],
    )
    def test_encode_str_caesar(self, text, shift, expected):
        assert encode_str_caesar(text, shift) == expected

    def test_encode_file(self, tmp_path_factory: pytest.TempPathFactory):
        text = "Hello\nHello\nHello\nHello, World!"
        expected_encoded_text = "Ifmmp\nJgnnq\nKhoor\nLipps, Asvph!"

        tmp_dir = tmp_path_factory.mktemp("temp_dir")
        tmp_source_file = tmp_dir / "source_file.txt"
        tmp_source_file.write_text(text)
        tmp_cipher_file = tmp_dir / "cipher_file.txt"
        tmp_cipher_file.touch()

        encode_file_caesar(tmp_source_file.absolute(), tmp_cipher_file.absolute())

        assert tmp_cipher_file.read_text() == expected_encoded_text

    def test_encode_file_twice(self, tmp_path_factory: pytest.TempPathFactory):
        first_text = "I'm not clever!"
        expected_first_cipher_text = "J'n opu dmfwfs!"
        second_text = "I'm just kidding. I'm very clever, HA-HA"
        expected_second_cipher_text = "J'n kvtu ljeejoh. J'n wfsz dmfwfs, IB-IB"

        tmp_dir = tmp_path_factory.mktemp("temp_dir")
        tmp_source_file = tmp_dir / "source_file.txt"
        tmp_source_file.write_text(first_text)
        tmp_cipher_file = tmp_dir / "cipher_file.txt"
        tmp_cipher_file.touch()

        encode_file_caesar(tmp_source_file.absolute(), tmp_cipher_file.absolute())
        first_cipher_text = tmp_cipher_file.read_text()

        tmp_source_file.write_text(second_text)
        encode_file_caesar(tmp_source_file.absolute(), tmp_cipher_file.absolute())
        second_cipher_text = tmp_cipher_file.read_text()

        assert first_cipher_text == expected_first_cipher_text
        assert second_cipher_text == expected_second_cipher_text
