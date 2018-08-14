import sys
from pprint import pprint
class Song(object):
    def __init__(self, song):
        # Available keys: id, lang, name, text, url
        for key, value in song.items():
            self.__dict__[key] = value

class Artist(object):
    def __init__(self, artist):
        # Available keys: id, name, url, pic_small
        # pic_medium, rank, top_lyrics, albums
        # genre and related
        for key, value in artist.items():
            self.__dict__[key] = value

class Rank(object):
    def rank(rank):
        return {key: value for key, value in rank.items()}

class Genre(object):
    def genre(genre):
        return [genre[x] for x in range(len(genre))]

class Related(object):
    def related(related):
        return [related[x] for x in range(len(related))]

class Toplyrics(object):
    def top_lyrics(top_lyrics):
        return [top_lyrics[x] for x in range(len(top_lyrics))]

class Albums(object):
    def albums(albums):
        return [albums[x] for x in range(len(albums))]
