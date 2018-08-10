#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, sys, classes
from pprint import pprint

"""
Wrapper for vagalume lyrics search
"""

api_base_url = 'https://api.vagalume.com.br/'
api_base_url_auth = 'https://api.vagalume.com.br/search.php'

class Main():
    def __init__(self, artist_name):
        self.name = artist_name


def api_request():

        api_search = api_base_url + artist_name + '/index.js'

        try:
            response = requests.get(api_search)
        except Exception as e:
            print("An error ocurred in get request: {}".format(e))
            sys.exit(0)

        data = response.json()
        return classes.Artist(data['artist'])

def get_rankpos(name):
    print("The rankd")
    rank_raw = self.connector.get_rank()
    print(rank_raw)

name = input("Name of the artist: ")
api_request(name)
get_rankpos(name)
