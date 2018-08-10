#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, sys
import classes as cl
from pprint import pprint

"""
Wrapper for vagalume lyrics search
"""

def search_method(artist_name, song_name=None):

    # Api base url
    API_URL = 'https://api.vagalume.com.br/' + artist_name + '/index.js'

    # URL params
    params = {
        'art': artist_name,
        'mus': song_name
    }

    # Try to get artist data
    try:
        response = requests.get(API_URL)
    except Exception as e:
        print("An error ocurred in get request: {}".format(e))
        sys.exit(0)

    # Parse data
    data = response.json()
    pprint(data['artist']['rank'])
    sys.exit(0)

search_method("dkapwokdapodkaopdk")
