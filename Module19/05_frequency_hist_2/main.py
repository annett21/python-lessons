def inverted_dict(text):
    updated_text = {}
    for key, value in text.items():
        if value not in updated_text:
            updated_text[value] = []
        updated_text[value].append(key)
    return updated_text


text = input("Введите текст: ")

new_text = {}

for letter in text:
    new_text[letter] = text.count(letter)
print("Оригинальный словарь частот:", new_text)


print("Инвертированный словарь частот:", inverted_dict(new_text))
