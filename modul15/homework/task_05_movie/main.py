from typing import List, Tuple


def get_input_parameters() -> List[str]:
    """
    Gets a list of favorite movies.
    """
    user_input = input("How many movies do you wanna add to favorites? ")

    try:
        len_of_favorites_list = int(user_input)
    except ValueError:
        len_of_favorites_list = 1

    if len_of_favorites_list < 1:
        len_of_favorites_list = 1

    favorite_movies: List[str] = []
    for _ in range(len_of_favorites_list):
        user_input = input("Enter the name of a movie: ")
        favorite_movies.append(user_input)

    return favorite_movies


def display_result(favorite_movies: List[str], unavailable_movies: List[str]) -> None:
    """
    Prints the list of unavailable movies and the list of favorite movies.
    """
    for movie in unavailable_movies:
        print(f'Warning: there is not "{movie}" movie :(')
    print("Your list of favorite movies:", ", ".join(favorite_movies))


def add_favorite_movies(
    new_favorite_movies: List[str], available_movies: List[str]
) -> Tuple[List[str], List[str]]:
    """
    Adds movies to the favorite list.

    Returns two lists. First -- favorite movies. Second -- unavailable movies.
    """
    return (
        [movie for movie in new_favorite_movies if movie in available_movies],
        [movie for movie in new_favorite_movies if movie not in available_movies],
    )


if __name__ == "__main__":
    available_movies = [
        "Крепкий орешек",
        "Назад в будущее",
        "Таксист",
        "Леон",
        "Богемская рапсодия",
        "Город грехов",
        "Мементо",
        "Отступники",
        "Деревня",
    ]
    new_favorite_movies = get_input_parameters()
    favorite_movies, unavailable_movies = add_favorite_movies(
        new_favorite_movies, available_movies
    )
    display_result(favorite_movies, unavailable_movies)
