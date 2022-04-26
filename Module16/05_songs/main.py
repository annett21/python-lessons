violator_songs = [
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

amount_of_songs = int(input("How many songs you want to chose? "))

music_time = 0

for i in range(1, amount_of_songs + 1):
    name_of_song = input(f"{i} song name: ")
    for song in range(0, len(violator_songs)):
        if violator_songs[song][0] == name_of_song:
            music_time += violator_songs[song][1]


print(f"Total songs time: {music_time:.4} minutes")
