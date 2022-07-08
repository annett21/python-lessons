import os
import string

alphabet = string.ascii_lowercase


# with open("Module22/06_paranoia/text.txt") as f:
#     text = f.read().split("\n")

# raw = ""
# for line, word in enumerate(text):
#     for letter in word:
#         if letter.isupper():
#             i = alphabet_upper.find(letter)
#             raw += alphabet_upper[(i + (line + 1)) % 26]
#         else:
#             i = alphabet_lower.find(letter)
#             raw += alphabet_lower[(i + (line + 1)) % 26]
#     raw += "\n"

# with open("Module22/06_paranoia/cipher.txt", "w") as new_file:
#     new_file.write(raw)


def encode_letter_caesar(letter: str, shift: int) -> str:
    # Encodes one letter
    pass


def encode_str_caesar(text: str, shift: int) -> str:
    # Encodes small text
    pass


def encode_file_caesar(abs_source_file_path: str, abs_cipher_file_path: str) -> None:
    # Reads source file line by line, encodes each line and writes to cipher file
    # https://stackoverflow.com/a/1073814
    pass


if __name__ == "__main__":
    source_file_path = "Module22/task_06_paranoia/text.txt"
    abs_source_file_path = os.path.abspath(source_file_path)

    cipher_file_path = "Module22/task_06_paranoia/cipher_text.txt"
    abs_cipher_file_path = os.path.abspath(cipher_file_path)

    encode_file_caesar(abs_source_file_path, abs_cipher_file_path)
