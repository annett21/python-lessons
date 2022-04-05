
numbers = int(input('Кол-во чисел в списке: '))

list_of_num = []

for num in range(1, numbers + 1):
    numm = int(input(f'Введите {num} число: '))
    list_of_num.append(numm)

devider = int(input('Введите делитель: '))

index_summ = 0

for numm in list_of_num:
    if numm % devider == 0:
        index = list_of_num.index(numm)
        print(f'Индекс числа {numm}:', index)
        index_summ += index

print('Сумма индексов:', index_summ)

