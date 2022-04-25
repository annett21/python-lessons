def int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Введите целое число.")


list_length = int_input("Количество чисел: ")

input_sequence = []
for _ in range(list_length):
    input_sequence.append(int_input("Число: "))

palindrome_sequence = input_sequence.copy()
for index in range(len(input_sequence)):
    carrent_number = palindrome_sequence[index]
    if palindrome_sequence != palindrome_sequence[::-1]:
        palindrome_sequence.insert(len(palindrome_sequence) - index, carrent_number)

print("Последовательность:", input_sequence)
print("Нужно приписать чисел:", len(palindrome_sequence) - len(input_sequence))
print("Сами числа:", palindrome_sequence[len(input_sequence) :])
