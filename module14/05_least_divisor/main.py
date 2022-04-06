
number = int(input('Введите число: '))

for i in range(2, number + 1):
    if number % i == 0:
        print('Наименьший делитель, отличный от единицы:', i)
        break

