import requests, sys, classes, os
from pprint import pprint

"""
Wrapper for vagalume lyrics search
"""

class ApiRequest():

    def __init__(self, artist_name):

        self.__artist = artist_name
        api_search = 'https://vagalume.com.br/' + self.__artist + '/index.js'

        try:
            response = requests.get(api_search)
        except Exception as e:
            print("An error ocurred in get request: {}".format(e))
            sys.exit(0)

        raw = response.json()
        self.__conn = classes.Artist(raw['artist'])

    # Return most acessed musics by artist
    def get_n_music_acessed(self, number):
        lyrics = self.__conn.get_top_lyrics()
        if number == "all":
            return lyrics
        else:
            if isinstance(number, int) and number >= 1:
                return lyrics[:number]
            else:
                raise ValueError('Please, use a number higher than 0.')

    def get_artist_position(self):
        rank = self.__conn.get_rank()
        return rank['pos']

    def get_artist_last_album(self):
        albums = self.__conn.get_albums()
        return albums[0]
