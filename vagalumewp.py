import requests, sys, classes, os, re
from pprint import pprint

"""
Wrapper for vagalume lyrics search
"""

class ApiRequest():

    def __init__(self, artist, song):
        self.__artist = artist
        self.__song = song

    def main(self):
        # API Urls
        api_url_v1 = r'https://api.vagalume.com.br'
        api_search = api_url_v1 + r'/search.php'
        api_url_v2 = r'https://vagalume.com.br/' + self.__artist + '/index.js'

        # API Params
        params = {
        'art': self.__artist,
        'mus': self.__song
        }

        # Data for response 1 - Treatment of song
        response1 = api_request(api_search, params)

        # Validate artist and song
        check_response(response1)

        # Initialize song constructor
        self.__conn1 = classes.Song(response1['mus'][0])

        # Data for response 2 - Treat everything else
        response2 = api_request(api_url_v2)

        self.__conn2 = classes.Artist(response2['artist'])

    # Return most acessed musics by artist
    def get_n_music_acessed(self, number):
        lyrics = self.__conn2.get_top_lyrics()
        if number == "all":
            return lyrics
        else:
            if isinstance(number, int) and number >= 1:
                return lyrics[:number]
            else:
                raise ValueError('Please, use a number higher than 0.')

    def get_artist_position(self):
        rank = self.__conn2.get_rank()
        return rank['pos']

    def get_artist_last_album(self):
        albums = self.__conn2.get_albums()
        return albums[0]

    def get_frequent_words(self):
        song = self.__conn1.get_text()
        wordlist = song.split()

        file = open('stop-words/portuguese.txt', 'r')
        stopword_br = file.readlines()
        file.close()

        result = list(set(wordlist) - set(stopword_br))
        common =  max(set(result), key=result.count)
        return common

def check_response(response):
    error_msg = None

    if response['type'] == 'notfound':
        error_msg = 'Artist not found! Try again.'

    if response['type'] == 'song_notfound':
        error_msg = 'Song not found! Try again.'

    if error_msg:
        print(error_msg)
        sys.exit(0)
    else:
        return True

def api_request(url, params=None):
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        print("An error ocurred in get request: {}".format(e))
        sys.exit(0)
