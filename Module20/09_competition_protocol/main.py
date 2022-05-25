def replace_item(d, word):
    for place, (_, names) in d.items():
        if names == word:
            d[place] = (0, 0)


notes = int(input("Сколько записей вносится в протокол? "))

competition_data = {}

print("Записи (результат и имя):")
for i_note in range(1, notes + 1):
    points, nickname = input(f"{i_note}-я запись: ").split()
    competition_data[i_note] = (int(points), nickname)

print("Итоги соревнований:")
for i in range(1, 4):
    win_score, win_name = max(competition_data.values(), key=lambda t: t[0])
    replace_item(competition_data, win_name)
    print(f"{i}-е место.", win_name, f"({win_score})")
