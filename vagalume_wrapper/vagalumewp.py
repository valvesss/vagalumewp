import requests, sys, os, re
from pprint import pprint
import vagalume_objects as vgo

"""
Wrapper for vagalume lyrics search
"""

class ApiRequest():

    def __init__(self, artist, song):
        self.__artist = artist
        self.__song = song

    def main(self):
        # API Urls
        api_url_v1 = r'https://api.vagalume.com.br/search.php'
        api_url_v2 = r'https://vagalume.com.br/' + self.__artist + '/index.js'

        # API Params
        params = {
        'art': self.__artist,
        'mus': self.__song
        }

        response1 = api_request(api_url_v1, params)
        self.conn_song = vgo.Song(response1['mus'][0])
        response2 = api_request(api_url_v2)
        self.conn_artist = vgo.Artist(response2['artist'])

    # Return most acessed musics by artist
    def get_n_music_acessed(self, number):
        lyrics = self.conn_artist.__dict__['toplyrics']['item']
        if number == "all":
            return lyrics
        else:
            if isinstance(number, int) and number >= 1:
                return lyrics[:number]
            else:
                raise ValueError('Please, use a number higher than 0.')

    def get_artist_position(self):
        rank = self.conn_artist.__dict__['rank']
        return rank['pos']

    def get_artist_last_album(self):
        albums = self.conn_artist.__dict__['albums']['item']
        return albums[0]

    def get_frequent_words(self):
        song = self.conn_song.__dict__['name']
        wordlist = song.split()

        file = open('../stop-words/portuguese.txt', 'r')
        stopword_br = file.readlines()
        file.close()

        result = list(set(wordlist) - set(stopword_br))
        common =  max(set(result), key=result.count)
        return common

def check_response(response):

    if 'type' in response.keys() and response['type'] == 'notfound':
        raise ValueError('Artist not found! Try again.')

    if 'type' in response.keys() and response['type'] == 'song_notfound':
        raise ValueError('Song not found! Try again.')

    else:
        return True

def api_request(url, params=None):

    response = requests.get(url, params=params).json()
    check_response(response)
    return response
