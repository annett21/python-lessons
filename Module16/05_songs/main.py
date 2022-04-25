import random
from typing import Any


violator_songs: list[list[Any]] = [
    ["World in My Eyes", 4.86],
    ["Sweetest Perfection", 4.43],
    ["Personal Jesus", 4.56],
    ["Halo", 4.9],
    ["Waiting for the Night", 6.07],
    ["Enjoy the Silence", 4.20],
    ["Policy of Truth", 4.76],
    ["Blue Dress", 4.29],
    ["Clean", 5.83],
]

handy_songs: dict[str, float] = {k: v for k, v in violator_songs}

for _ in range(3):
    user_input = input("How many songs? ")
    try:
        songs_count = int(user_input)
        if songs_count < 1 or songs_count > len(violator_songs):
            raise ValueError
    except ValueError:
        print(f"Enter a positive integer number between 1 and {len(violator_songs)}.")
        continue
    break
else:
    songs_count = 3

songs_playing_time = 0.0
for song_number in range(1, songs_count + 1):
    song = input(f"The name of {song_number} song: ")

    if song not in handy_songs:
        song = random.choice(list(handy_songs))
        print("The chosen song is not on the list.")
        print("The song was chosen randomly:", song)

    songs_playing_time += handy_songs[song]

print("The total playing time of chosen songs:", songs_playing_time, "minutes")
