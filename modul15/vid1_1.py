numbers = [3,7,5]

while True:

 number = int(input('Новое число: '))

 numbers.append(number)

 print('Текущий список чисел:', numbers)

 for number in numbers:

   print(number ** 2, number ** 3, number ** 4)

 print()