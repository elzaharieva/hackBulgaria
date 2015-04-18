import pprint
from random import randint
from tabulate import tabulate
import os
import json
import sys
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import os
import glob


def length_validation(length):
    if length == "":
        return True
    elif len(length) > 3 and length[-3] == ':':
        return True
    elif len(lenght) > 6 and length[-6] == ':':
        return True
    else:
        return False


class Song:

    def __init__(self, title="", artist="", album="", length=""):

        if length_validation(length):
            self.title = title
            self.artist = artist
            self.album = album
            self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self. album, self.length)

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length

    def __hash__(self):
        return hash(self.title)

    def length_func(self, seconds=False, minutes=False, hours=False):
        if seconds == True:
            return self.length[-2:]
        elif minutes == True:
            if len(self.length) > 4:
                return self.length[-5:-3]
            else:
                return self.length[:-3]
        elif hours == True:
            return self.length[:-6]
        else:
            return self.length


class Playlist:

    played = []

    def __init__(self, name="", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.song_list = []
        self.played = []

    def add_song(self, song):
        if song not in self.song_list:
            self.song_list.append(song)

    def remove_song(self, song):
        if song in self.song_list:
            self.song_list.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def artists(self):
        my_artists = {}
        for song in self.song_list:
            key = song.artist
            if key not in my_artists:
                my_artists[key] = 1
            else:
                my_artists[key] += 1
        return my_artists

    def get_index(self, list, a):
        index = 0
        while index < (len(list)):
            if list[index] != a:
                index += 1
            return index

    def total_length(self):
        total_sec = 0
        total_min = 0
        total_hr = 0
        for song in self.song_list:
            total_sec += int(song.length_func(seconds=True))
            total_min += int(song.length_func(minutes=True))
            if len(song.length_func()) > 5:
                total_hr += int(song.length_func(hours=True))
        while total_sec >= 60:
            total_sec -= 60
            total_min += 1
        while total_min >= 60:
            total_min -= 60
            total_hr += 1
        return "{}:{}:{}".format(total_hr, total_min, total_sec)

    def next_song(self, current_song):
        if self.shuffle == False:
            if current_song == self.song_list[-1]:
                if self.repeat == False:
                    return "No more songs to play"
                else:
                    current_song = self.song_list[0]
            else:
                current_song = self.song_list[
                    self.get_index(self.song_list, current_song) + 1]
                return current_song
        else:
            self.played.append(current_song)
            if len(self.played) == len(self.song_list):
                if self.repeat == False:
                    return "No more songs to play"
                else:
                    self.played = []
                    current_song = self.song_list[
                        randint(0, len(self.song_list) - 1)]
            while current_song in self.played:
                current_song = self.song_list[
                    randint(0, len(self.song_list) - 1)]
            return current_song

    def pprint_playlist(self):
        pptable = []
        snum = 0
        headers = ["№", "Artist", "Album", "SongTitle", "length"]
        for song in self.song_list:
            snum += 1
            pptable.append(
                [snum, song.artist, song.album, song.title, song.length])
        print (tabulate(pptable, headers, tablefmt="fancy_grid"))

    def save(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        directory = 'playlists/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        plistname = path + '/' + directory + \
            self.name.replace(" ", "-") + ".json"
        save_data = {'name': self.name, 'songs': []}
        for song in self.song_list:
            save_data['songs'].append(song.__dict__)
        file = open(plistname, "w")
        file.write(json.dumps(save_data))
        file.close()

    @staticmethod
    def load(path):
        with open(path, 'r') as load_file:
            load_data = json.load(load_file)
            loaded_playlist = Playlist(load_data['name'])
            for song_data in load_data['songs']:
                song = Song(song_data['title'], song_data[
                            'artist'], song_data['album'], song_data['length'])
                loaded_playlist.add_song(song)
        return loaded_playlist


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def func(self, a):
        hours = 0
        minutes = 0
        while (a >= 3600):
            a -= 3600
            hours += 1
        while (a >= 60):
            a -= 60
            minutes += 1
        if hours > 0:
            string = str(hours) + ':' + str(minutes) + ':' + str(a)
        else:
            string = str(minutes) + ':' + str(a)
        return string

    def generate_playlist(self, playlist_name="", playlist_shuffle=False, playlist_reppeat=True):
        pl = Playlist(playlist_name, playlist_reppeat, playlist_shuffle)
        direc = glob.glob(self.path + "/*.mp3")
        for b in direc:
            filename = b[19:]

            mp3file = MP3(filename, ID3=EasyID3)
            songlen = int(mp3file.info.length)
            s = Song(title=mp3file['title'], artist=mp3file[
                     'artist'], album=mp3file['album'], length=self.func(songlen))
            pl.add_song(s)

        return pl


