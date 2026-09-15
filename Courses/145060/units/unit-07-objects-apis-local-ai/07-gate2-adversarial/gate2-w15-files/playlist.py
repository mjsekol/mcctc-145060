# playlist.py
#
# Builds a playlist from songs and reports on it. Written from the spec in the
# Gate 2 handout. It runs and looks reasonable. Your job is to find what is wrong.

class Song:
    """One song: its title, artist, and length in seconds."""

    def __init__(self, title, artist, seconds):
        self.title = title
        self.artist = artist
        self.seconds = seconds


class Playlist:
    """A named playlist of songs."""

    songs = []          # the songs on this playlist

    def __init__(self, name):
        self.name = name
        self.length_minutes = 0

    def add_song(self, song):
        # Add a song to the playlist.
        self.songs.append(song)
        return f"Added {song.title}."

    def total_minutes(self):
        # Add up the length of every song, in minutes, and return whole minutes.
        self.length_minutes = 0
        for song in self.songs:
            self.length_minutes += song.seconds
        return self.length_minutes // 60

    def longest(self):
        # Find the longest song by comparing every song to every other.
        longest_song = self.songs[0]
        for song in self.songs:
            for other in self.songs:
                if other.seconds > longest_song.seconds:
                    longest_song = other
        return longest_song.title

    def summary(self):
        return f"{self.name}: {len(self.songs)} songs, {self.total_minutes()} minutes total."


def main():
    party = Playlist("Party Mix")
    party.add_song(Song("Sunroof", "Nicky Youre", 163))
    party.add_song(Song("As It Was", "Harry Styles", 167))
    party.add_song(Song("Heat Waves", "Glass Animals", 238))
    print(party.summary())


if __name__ == "__main__":
    main()
