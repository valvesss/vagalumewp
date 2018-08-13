#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, sys, classes
from pprint import pprint

"""
Wrapper for vagalume lyrics search
"""


# def api_request(artist, song=None):
#
#     params = {}
#     params['art'] = artist
#     params['mus'] = song
#
#     response = requests.get(api_base_url, params=params)
#     print(response)
#     sys.exit(0)
#     data = response.json()
#     return True

def get_artist(name, limit=None):

    api_base_url = 'https://api.vagalume.com.br/search.php'
    api_base_url += '.art?q=' + name
    
    if limit:
        api_base_url += '&limit=' + limit

    response = requests.get(api_base_url)
    print(type(response))

get_artist("rihanna")
# def api_request(artist_name):
#
#         api_search = api_base_url + artist_name + '/index.js'
#
#         try:
#             response = requests.get(api_search)
#         except Exception as e:
#             print("An error ocurred in get request: {}".format(e))
#             sys.exit(0)
#
#         data = response.json()
#         return classes.Artist(data['artist'])
#
# def get_rankpos(conn, name):
#     rank_raw = conn.get_genre()
#     print("The rank: ", rank_raw)
#
# name = input("Name of the artist: ")
# conn = api_request(name)
# get_rankpos(conn, name)
