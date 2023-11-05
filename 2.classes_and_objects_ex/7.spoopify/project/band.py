from typing import List
from project.song import Song
from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, _album: Album):
        if _album in self.albums:
            return f"Band {self.name} already has {_album.name} in their library."
        self.albums.append(_album)
        return f"Band {self.name} has added their newest album {_album.name}."

    def remove_album(self, name: str):
        for album_obj in self.albums:
            if album_obj.name == name:
                if album_obj.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(album_obj)
                    return f"Album {name} has been removed."
        else:
            return f"Album {name} is not found."

    def details(self):
        info = [f'Band {self.name}']
        for alb in self.albums:
            info.append(alb.details())
        return '\n'.join(info)


# Test code!
song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())



