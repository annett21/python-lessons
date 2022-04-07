from typing import List


def display_result(participants_names: List[str]) -> None:
    """
    Prints paticipants' names.
    """
    print("First day:", participants_names)


def get_participants_names(names: List[str]) -> List[str]:
    """
    Returns participants' names on even positions.
    """
    return [name for name in names if names.index(name) % 2 == 0]


if __name__ == "__main__":
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )
    display_result(participants_names)
