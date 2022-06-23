from collections import Counter


def read_file(file_path):
    with open(file_path) as files:
        text = files.read()
    return text


def count_words(text):
    amount_of_words = 0
    for line in text:
        amount_of_words += len(line.split())
    return amount_of_words


def count_letters(text):
    counter = 0
    for char in text:
        if char.isalpha():
            counter += len(char)
    return counter


def find_unique_letter(text):
    text = text.lower()
    new_line = ""
    for letter in text:
        if letter.isalpha():
            new_line += letter
    c = Counter(new_line)
    unique_letter = c.most_common()[:-2:-1]
    return unique_letter[0][0]


path = "Module22/02_zen_of_python/zen.txt"
text = read_file(path)
full_text = text.split(sep="\n")

print("Количество букв в файле: ", count_letters(text))
print("Количество слов в файле: ", count_words(full_text))
print("Количество строк в файле:", len(full_text))
print("Наиболее редкая буква: ", find_unique_letter(text))
