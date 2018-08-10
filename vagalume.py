#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, sys
from decouple import config
from pprint import pprint

"""
Wrapper for vagalume lyrics search
"""

def search_method(artist_name, song_name=None):

    API_URL = 'https://api.vagalume.com.br/' + artist_name + '/index.js'

    params = {
        'art': artist_name,
        'mus': song_name
    }

    try:
        response = requests.get(API_URL)
    except Exception as e:
        print("An error ocurred in get request: ", e)

    data = response.json()
    pprint(data['artist']['rank'])
    sys.exit(0)

# class Apirequest(object):
#     def __init__(self, artist):
#         self.id = artist['id']
#         self.name = artist['name']
#         self.url = artist['url']
#
#     def get_artist(self):
#         pprint(artist)

search_method("dkapwokdapodkaopdk")
