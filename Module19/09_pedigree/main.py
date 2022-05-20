# num = int(input("Введите количество человек: "))

# names = {}

# for i in range(1, num):
#     name = input(f"{i} пара: ").split()
#     if name[1] not in names:
#         names[name[1]] = []
#     names[name[1]].append(name[0])

# print(names)

names = {
    "Peter_I": ["Alexei", "Anna", "Elizabeth"],
    "Alexei": ["Peter_II"],
    "Anna": ["Peter_III"],
    "Peter_III": ["Paul_I"],
    "Paul_I": ["Alexander_I", "Nicholaus_I"],
}

# print("Высота» каждого члена семьи:", )
