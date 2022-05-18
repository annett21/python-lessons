num = int(input("Введите количество пар слов: "))
synonyms = {}

for i in range(1, num + 1):
    word_pair = input(f"{i} пара: ")
    words = word_pair.split(" - ")
    synonyms[words[0]] = words[1]


def find_synonyms(word):
    word = word.lower()
    for key, value in synonyms.items():
        if word == key.lower():
            return value
        elif word == value.lower():
            return key


word_check = input("Введите слово: ")

while not find_synonyms(word_check):
    print("Такого слова в словаре нет.")
    word_check = input("Введите слово: ")

print("Синоним:", find_synonyms(word_check))
