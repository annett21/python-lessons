num = int(input('Введите число: '))

def sum_digits(num):
    return sum(map(int, str(num)))

def num_of_digits(num):
    return len(str(num))

print('Сумма цифр:', sum_digits(num))
print('Кол-во цифр в числе:', num_of_digits(num))

print('Разность суммы и кол-ва цифр:', sum_digits(num) - num_of_digits(num))