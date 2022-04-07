from typing import List


def get_input_parameters() -> List[int]:
    """
    Gets list of video cards.
    """
    for _ in range(3):
        user_input = input("Quantity of video cards: ")

        try:
            quantity_cards = int(user_input)
        except ValueError:
            print("Enter an integer number.")
            continue

        if quantity_cards < 1:
            print("Enter a number greather than 0.")
            continue
        else:
            break
    else:
        quantity_cards = 5
        print(f"Quantity of video cards: {quantity_cards}")

    cards = []
    for index in range(quantity_cards):
        while True:
            user_input = input(f"Video card {index + 1}:")
            try:
                cards.append(int(user_input))
            except ValueError:
                continue
            else:
                break

    return cards


def display_result(old_video_cards: List[int], new_video_cards: List[int]) -> None:
    """
    Prints all old cards and left cards.
    """
    print("List of old video cards:", ", ".join(map(str, old_video_cards)))
    print("New list of video cards:", ", ".join(map(str, new_video_cards)))


def select_video_cards(video_cards: List[int]) -> List[int]:
    """
    Deletes the best cards (deletes maximum numbers from the list).
    """
    best_card = max(video_cards)
    return [card for card in video_cards if card != best_card]


if __name__ == "__main__":
    video_cards = get_input_parameters()
    result_video_cards = select_video_cards(video_cards)
    display_result(video_cards, result_video_cards)
