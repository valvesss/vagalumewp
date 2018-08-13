#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vagalumewp, os
from pprint import pprint

os.system('clear')

# Ask for an artist name
name = input("Name of the artist to search: ")

# Start connection to object with the given name
connection = vagalumewp.ApiRequest(name)

# Give informations about the artist
print("Informations about {} !\n".format(name.title()))

# Print the number of music most acessed
print("Set a number to retrieve musics most acessed!")
pprint(connection.get_n_music_acessed(int(input("Number: "))))

# Print the artist position in vagalume rank
print("Artist position in vagalume rank:", connection.get_artist_position())

# Print the artist last album
print("Artist last album:", connection.get_artist_last_album())
