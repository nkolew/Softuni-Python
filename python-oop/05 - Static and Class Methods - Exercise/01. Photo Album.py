import math
from typing import List, Union


class PhotoAlbum:
    pages: int
    photos: List[List[str]]

    __photos: Union[List[List[str]], List[List[None]]]

    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.__photos = [self.__class__.PHOTOS_PER_PAGE*[None]
                         for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> 'PhotoAlbum':
        pages = math.ceil(photos_count/4)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for i, row in enumerate(self.__photos, start=1):
            for j, photo in enumerate(row, start=1):
                if not photo:
                    self.__photos[i-1][j-1] = label
                    return f'{label} photo added successfully on page {i} slot {j}'

        return 'No more free slots'

    @property
    def photos(self):
        result = []
        for i in range(len(self.__photos)):
            row = []
            for j in range(len(self.__photos[i])):
                if self.__photos[i][j]:
                    row.append(self.__photos[i][j])
            result.append(row)

        return result

    def display(self) -> str:
        message = []
        NL = '\n'
        SEP = 11*'-'

        message.append(SEP)

        for i in range(len(self.__photos)):
            row = []
            for j in range(len(self.__photos[i])):
                if self.__photos[i][j]:
                    row.append('[]')
            message.append(' '.join(row))
            message.append(SEP)

        return NL.join(message)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
