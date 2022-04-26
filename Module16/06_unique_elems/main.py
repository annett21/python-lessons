from collections import Counter

base_list = []
side_list = []

for num in range(1, 3 + 1):
    base_num = int(input(f"Enter {num} for the base list: "))
    base_list.append(base_num)

for numb in range(1, 7 + 1):
    side_num = int(input(f"Enter {numb} for the side list: "))
    side_list.append(side_num)

print("Base list:", base_list)
print("Side list", side_list)

base_list.extend(side_list)
print("Updated base list with unique elements", list(Counter(base_list)))
