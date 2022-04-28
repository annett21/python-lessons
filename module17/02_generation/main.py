from random import randint

number = int(input("Enter the lenth of list: "))

print(
    "Result:",
    [1 if randint(1, 100) % 2 == 0 else randint(1, 100) % 5 for _ in range(number)],
)
