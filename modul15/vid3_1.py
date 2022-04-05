
import re

text = input('Введите стороку: ')
text = list(text)

text1 = ''.join(text)

re.sub(':', ';', text1)

print(text1)