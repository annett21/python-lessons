employees = int(input('Кол-во сотрудников в офисе: '))
employees_id = []

for _ in range(employees):
    id = int(input('ID сотрудника: '))
    employees_id.append(id)

check_id = int(input('Какой ID ищем? '))

if check_id in employees_id:
    print('Сотрудникак трудится не покладая рук!')
else:
    print('Сотрудник не работает!')
