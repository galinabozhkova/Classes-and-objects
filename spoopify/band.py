from spoopify.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for el in self.albums:
            if el.name == album_name:
                if el.published:
                    return "Album has been published. It cannot be removed."
            self.albums.remove(el)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}"
        for el in self.albums:
            result += "\n" + f"{el.details()}"
        return result


