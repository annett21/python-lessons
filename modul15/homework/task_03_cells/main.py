def get_input_parameters():
    """
    Получаем набор клеток
    
    :return: набор клеток, например: [3, 0, 6, 2, 10]
    :rtype: List[int]
    """
    cells = []
    amount_of_cells = int(input('Кол-во клеток: '))
    for cell in range(1, amount_of_cells + 1):
        efficiency = int(input(f"Эффективность {cell} клетки: "))
        cells.append(efficiency)

    return cells



def display_result(bad_cells):
    """
    Выводим список клеток у которых значение меньше индекса
    
    :param cells: набор клеток, например: [0, 2]
    :type cells: List[int]
    """
    print("Неподходящие значения:", bad_cells)


def select_cells(cells):
    """
    Отбираем список клеток, у которых значение меньше индекса.
    
    :param cells: набор клеток, например: [3, 0, 6, 2, 10]
    :type cells: List[int]
    
    :return: набор подходящих клеток, например: [0, 2]
    :rtype: List[int]
    """
    bad_cells = []
    for cell in cells:
        if cells.index(cell) > cell:
            bad_cells.append(cell)

    return bad_cells


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат