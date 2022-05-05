text = input("Enter a string: ")

text = text.split()
length = [len(word) for word in text]

print("The longest word:", text[length.index(max(length))])
print("The length of this word:", max(length))
