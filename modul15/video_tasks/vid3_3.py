first_word = input('Введите 1 слово: ')
second_word = input('Введите 2 слово: ')
third_word = input('Введите 3 слово: ')

text = []

while True:
    current_word = input('Слово из теста: ')
    text.append(current_word)
    if current_word == 'end':
        break

print('Подсчет слов в тексте')
print(first_word, text.count(first_word))
print(second_word, text.count(second_word))
print(third_word, text.count(third_word))

