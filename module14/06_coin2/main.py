
print('Введите координаты монетки: ')

x = float(input('X: '))
y = float(input('Y: '))

r = int(input('Введите радиус: '))

def check_coin(x, y, r):
    c = x ** 2 + y ** 2
    return c <= r ** 2
   
if check_coin(x, y, r):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')