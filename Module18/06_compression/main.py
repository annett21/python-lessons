text = input("Enter a string: ")
counter = 1
line = ""

for index in range(1, len(text)):
    if text[index] != text[index - 1]:
        line += text[index - 1] + str(counter)
        counter = 1
    else:
        counter += 1
    if index == len(text) - 1:
        line += text[index] + str(counter)


print("Encoded string:", line)
