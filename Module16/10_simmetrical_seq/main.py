numbers = int(input("Кол-во чисел: "))
order = []

for _ in range(numbers):
    num = int(input("Число: "))
    order.append(num)

piece = order[:-1]
if order[-1] == order[-2]:
    piece = order[:-2]
    
print("Последовательность:", order)
print("Нужно приписать чисел:", len(piece))
print("Сами числа:", piece[::-1])
