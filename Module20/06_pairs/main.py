original_list = list(range(10))

print("Оригинальный список:", original_list)

new_list = [(x, x + 1) for x in range(0, 10, 2)]

# new_list = [(x, x + 1) for num in original_list for x in range(0, num, 2)]

print("Новый список:", new_list)
