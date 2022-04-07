from random import randint
from typing import List


def get_input_parameters() -> List[int]:
    """
    Gets a list of efficiency of cells by entering.
    """
    for _ in range(3):
        user_input = input("Quantity of cells: ")

        try:
            quantity_cells = int(user_input)
        except ValueError:
            print("Enter an integer number.")
            continue

        if quantity_cells < 1:
            print("Enter a number greather than 0.")
            continue
        else:
            break
    else:
        quantity_cells = 5
        print(f"Quantity of cells: {quantity_cells}")

    cells = []
    for index in range(quantity_cells):
        user_input = input(f"Efficiency of cell {index + 1} is ")
        try:
            cells.append(int(user_input))
        except ValueError:
            cells.append(randint(0, 10))
            print(f"Efficiency of cell {index + 1} is {cells[-1]}")

    return cells


def display_result(cells: List[int]) -> None:
    """
    Displays result. Suddenly)
    """
    print("Unsuitable values:", " ".join(map(str, cells)))


def select_cells(cells: List[int]) -> List[int]:
    """
    Filters cells. Returns cells with efficiency less than index.
    """
    # warning! works only if cells have unique efficiencies
    # return [cell for cell in cells if cell < cells.index(cell)]

    unsuitable_cells = []
    for index, cell in enumerate(cells):
        if cell < index:
            unsuitable_cells.append(cell)

    return unsuitable_cells


if __name__ == "__main__":
    cells = get_input_parameters()
    result_cells = select_cells(cells)
    display_result(result_cells)
