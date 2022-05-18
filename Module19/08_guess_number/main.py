max_number = int(input("Введите максимальное число: "))
yes_set = set()
no_set = set()

num = input("Нужное число есть среди вот этих чисел: ")

while num != "help":
    answer = input("Ответ Артёма: ")
    if answer == "Да" or answer == "yes":
        yes_set = set(num.split())
    elif answer == "Нет" or answer == "no":
        no_set = set(num.split())
    num = input("Нужное число есть среди вот этих чисел: ")


print("Артём мог загадать следующие числа:", yes_set.difference(no_set))
