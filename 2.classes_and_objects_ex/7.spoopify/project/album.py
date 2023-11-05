from typing import List, Tuple
from project.song import Song


class Album:
    def __init__(self, name: str, *args: Song):
        self.name = name
        self.published = False
        self.songs: List[Song] = [*args]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in list(map(lambda s: s.name, self.songs)):
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        [self.songs.remove(s) for s in self.songs if s.name == song_name]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f'Album {self.name}']
        for song in self.songs:
            info.append(f'== {song.get_info()}')
        return '\n'.join(info)
