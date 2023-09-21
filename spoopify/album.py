from spoopify.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(*songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if any([el.name == song.name for el in self.songs]):
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        for el in self.songs:
            if el.name == song_name:
                self.songs.remove(el)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}"
        for el in self.songs:
            result += "\n" + f"== {el.get_info()}"
        return result
