#!/usr/bin/env python3
import vagalumewp, os

os.system('clear')

# Ask for an artist name
name = input("Name of the artist to search: ")
song = input("Name of the song to search: ")

# Start connection to object with the given name and song
connection = vagalumewp.ApiRequest(name, song)

# Initialize constructors
connection.main()

# Give informations about the artist
print("Informations about {} !\n".format(name.title()))

# Print the number of music most acessed
print("Set a number to retrieve musics most acessed!", connection.get_n_music_acessed(input("Number: ")))


# Print the artist position in vagalume rank
print("\nArtist position in vagalume rank:", connection.get_artist_position())

# Print the artist last album
print("\nArtist last album:", connection.get_artist_last_album())

### WORKS NICE FOR BRAZILIANS SINGERS
# Print most frequent words in given music
print("\nArtist \"{}\" music most frequent word : {}".format(song,connection.get_frequent_word()))

## WORKING ON
# Print most frequent words for given last albums
print("\nArtist \"{}\" albums most frequent word : {}".format(song,connection.get_frequent_words()))
