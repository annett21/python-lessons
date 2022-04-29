text = input("Введите строку: ")
print(text[text.index("h") + 1 : text.rindex("h")][::-1])
