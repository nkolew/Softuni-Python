from song import Song
from typing import List


class Album:
    def __init__(self, name: str, *songs) -> None:
        self.name = name
        self.songs: List[Song] = list(songs)
        self.published = False

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return 'Cannot add songs. Album is published.'

        if song in self.songs:
            return f'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return f'Cannot remove songs. Album is published.'

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f'Removed song {song_name} from album {self.name}.'

        return 'Song is not in the album.'

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self) -> str:
        message = []
        nl = '\n'

        message.append(f'Album {self.name}')
        for song in self.songs:
            message.append(f'== {song.get_info()}')

        return nl.join(message) + nl
