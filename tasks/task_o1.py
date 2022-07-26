def devision_function(a, b):
    return a / b


def safe_input(input_str, error_str):
    while True:
        try:
            return int(input(input_str))
        except ValueError:
            print(error_str)


if __name__ == "__main__":
    wrong_number_error = "Необходимо вводить только целые числа!"

    while True:
        first_num = safe_input("Введите первое число: ", wrong_number_error)
        second_num = safe_input("Введите второе число: ", wrong_number_error)

        try:
            div = devision_function(first_num, second_num)
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
            continue

        print(div)
        break
