# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text = input("Введите сообщение: ")
step = int(input("Введите сдвиг: "))
raw = ""

for letter in text:
    i = alphabet.find(letter)
    if letter not in alphabet:
        raw += letter
    else:
        raw += alphabet[(i + step) % 33]
   
print("Зашифрованное сообщение:", raw)

