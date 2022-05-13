text = input("Message: ")

new_text = ""
reversed_word = ""
word = ""

for char in text:
    if char.isalpha():
        word += char
    else:
        reversed_word = word[::-1]
        new_text += reversed_word + char
        word = ""

print("Новое сообщение: ", new_text)
