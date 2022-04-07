from typing import List, Tuple


def get_input_parameters() -> Tuple[List[int], int]:
    """
    Gets a list of weights of containers and a weight of a new container.
    The weight of any container cannot be over 200.
    """
    user_input = input("How many containers are in stock? ")

    try:
        len_of_containers_list = int(user_input)
    except ValueError:
        len_of_containers_list = 10

    if len_of_containers_list < 1:
        len_of_containers_list = 10

    list_container_weights: List[int] = []

    for _ in range(len_of_containers_list):
        while True:
            user_input = input("Enter the weight of the container: ")

            try:
                weight = int(user_input)
            except ValueError:
                print("Error: enter an integer number.")
                continue

            if weight < 1:
                print("Error: the weight of the container cannot be less than 1.")
                continue
            if weight > 200:
                print("Error: the weight of the container cannot be over 200.")
                continue
            if list_container_weights and list_container_weights[-1] < weight:
                print(
                    "Error: the weight of the current container cannot be "
                    "greater than the weight of the previous container."
                )
                continue

            list_container_weights.append(weight)
            break

    new_container_weight = 0

    while True:
        user_input = input("Enter the weight of the new container: ")

        try:
            weight = int(user_input)
        except ValueError:
            print("Error: enter an integer number.")
            continue

        if weight < 1:
            print("Error: the weight of the container cannot be less than 1.")
            continue
        if weight > 200:
            print("Error: the weight of the container cannot be over 200.")
            continue

        new_container_weight = weight
        break

    return list_container_weights, new_container_weight


def display_result(serial_number_new_container: int) -> None:
    """
    Prints the number of the new container.
    """
    print("The number of the new container is", serial_number_new_container)


def search_serial_number_new_container(
    list_container_weights: List[int], new_container_weight: int
) -> int:
    """
    Searches the number of the new container.
    The list of container weights should be sorted by descending.
    The number of the new container will fit sorting.
    """
    for index, weight in enumerate(list_container_weights):
        if weight < new_container_weight:
            return index + 1
    return len(list_container_weights) + 1


if __name__ == "__main__":
    list_container_weights, new_container_weight = get_input_parameters()
    serial_number_new_container = search_serial_number_new_container(
        list_container_weights, new_container_weight
    )
    display_result(serial_number_new_container)
