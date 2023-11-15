class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4 if photos_count % 4 == 0 else int(photos_count // 4) + 1)

    def add_photo(self, label: str):
        for r in range(len(self.photos)):
            if len(self.photos[r]) < 4:
                self.photos[r].append(label)
                return f'{label} photo added successfully on page {r+1} slot {len(self.photos[r])}'
        return "No more free slots"

    def display(self):
        result = ['-' * 11]
        for element in self.photos:
            result.append(' '.join(['[]' for el in element]))
            result.append('-' * 11)
        return '\n'.join(result)


# Test code!
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
