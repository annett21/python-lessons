import string

alphabet_upper = string.ascii_uppercase
alphabet_lower = string.ascii_lowercase


with open("Module22/06_paranoia/text.txt") as f:
    text = f.read().split("\n")

raw = ""
for line, word in enumerate(text):
    for letter in word:
        if letter.isupper():
            i = alphabet_upper.find(letter)
            raw += alphabet_upper[(i + (line + 1)) % 26]
        else:
            i = alphabet_lower.find(letter)
            raw += alphabet_lower[(i + (line + 1)) % 26]
    raw += "\n"

with open("Module22/06_paranoia/cipher.txt", "w") as new_file:
    new_file.write(raw)
