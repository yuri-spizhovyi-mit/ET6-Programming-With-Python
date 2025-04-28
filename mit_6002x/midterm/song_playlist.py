# songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
songs = [
    ("Roar", 4.4, 4.0),
    ("Sail", 3.5, 7.7),
    ("Timber", 5.1, 6.9),
    ("Wannabe", 2.7, 1.2),
]


# return ['Roar','Wannabe','Timber']
def song_playlist(songs: list[tuple], max_size: float) -> list[str]:
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    song_list_to_play = []
    disc_space = max_size
    if songs[0][2] > max_size:
        return []
    elif songs[0][2] <= max_size:
        song_list_to_play.append(songs[0][0])
        disc_space -= songs[0][2]
    sorted_songs = sorted(songs[1:], key=lambda x: x[-1])
    for song in sorted_songs:
        if song[2] <= disc_space:
            song_list_to_play.append(song[0])
            disc_space -= song[2]

    return song_list_to_play


print(song_playlist(songs, 3))
