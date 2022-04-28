vowels = "аеёиоэюяуы"

text = input("Введите текст: ")

vowels_in_text = [vowel for vowel in text if vowel in vowels]

print("Список гласных букв:", vowels_in_text)
print("Длина списка:", len(vowels_in_text))
