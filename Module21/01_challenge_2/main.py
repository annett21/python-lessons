num = int(input("Введите num: "))


def output_numbers(num: int) -> None:
    if num != 1:
        output_numbers(num - 1)
    print(num)


def output_numbers_2(num: int, current_num: int = 1) -> None:
    print(current_num)
    if current_num == num:
        return
    output_numbers_2(num, current_num + 1)


output_numbers(num)
print("--__--")
output_numbers_2(num)
