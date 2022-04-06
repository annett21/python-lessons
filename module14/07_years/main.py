first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print(f'\nГода от {first_year} до {second_year} с тремя одинаковыми цифрами:')

for year in range(first_year, second_year + 1):
    year = list(str((year)))
    for digit in year[:2]:
        a = year.count(digit)
        if a == 3:
            print(''.join(year))
            break

