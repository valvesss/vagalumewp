#!/usr/bin/env python3
import vagalumewp, os

os.system('clear')

# Ask for an artist name
name = input("Name of the artist to search: ")
song = input("Name of the song to search: ")

# Start connection to object with the given name
connection = vagalumewp.ApiRequest(name, song)
connection.main()
connection.get_frequent_words()
