first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))

def duble_reverse(num):
    num_list = str(num).split('.')
    list_one = []
    for i in num_list:
        i = i[::-1]
        list_one.append(i)
    a = '.'.join(list_one)
    return float(a)

print('Первое число наоборот:', duble_reverse(first_num))
print('Второе число наоборот:', duble_reverse(second_num))
print('Сумма:', duble_reverse(first_num) + duble_reverse(second_num))