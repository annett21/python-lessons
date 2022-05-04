menu = "утиное филе;фланк-стейк;банановый пирог;плов"
print("Доступное меню:", menu)
new_menu = ", ".join(menu.split(sep=";"))
print(f"\nНа данный момент в меню есть: {new_menu}")