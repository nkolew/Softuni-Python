from song import Song
from typing import List


class Album:
    published = False

    def __init__(self, name: str, *songs) -> None:
        self.name = name
        self.songs: List[Song] = list(songs)

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return 'Cannot add songs. Album is published.'

        if song in self.songs:
            return f'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'
