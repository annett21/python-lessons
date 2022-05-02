alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text = input("Введите сообщение: ")
step = int(input("Введите сдвиг: "))
raw = ""

for letter in text:
    i = alphabet.find(letter)
    if letter not in alphabet:
        raw += letter
    else:
        raw += alphabet[i + step]
   
print("Зашифрованное сообщение:", raw)

