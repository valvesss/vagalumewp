class Song(object):
    def __init__(self, song):
        self.__id = song['id']
        self.__lang = song['lang']
        self.__name = song['name']
        self.__text = song['text']
        self.__url = song['url']

    def get_text(self):
        return self.__text

    def get_name(self):
        return self.__name

class Artist(object):
    def __init__(self, artist):
        self.__id = artist['id']
        self.__name = artist['desc']
        self.__url = artist['url']
        self.__pic_small = artist['pic_small']
        self.__pic_medium = artist['pic_medium']
        self.__rank = Rank.rank(artist['rank'])
        self.__top_lyrics = Toplyrics.top_lyrics(artist['toplyrics']['item'])
        self.__albums = Albums.albums(artist['albums']['item'])
        self.__genre = Genre.Genre(artist['genre'])
        self.__related = Related.Related(artist['related'])

    def get_rank(self):
        return self.__rank

    def get_top_lyrics(self):
        return self.__top_lyrics

    def get_albums(self):
        return self.__albums

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def get_pic_small(self):
        return self.__pic_small

    def get_pic_medium(self):
        return self.__pic_medium

    def get_genre(self):
        return self.__genre

    def get_related(self):
        return self.__related

class Rank(object):
    def rank(rank):
        artist_rank = {}
        for key, value in rank.items():
            artist_rank[key] = value
        return artist_rank

class Genre(object):
    def genre(genre):
        artist_genres = []
        for x in range(len(genre))
            artist_genres.append(genre[x])
        return artist_genres

class Related(object):
    def related(related):
        artist_relates = []
        for x in range(len(related))
            artist_relates.append(related[x])
        return artist_relates

class Toplyrics(object):
    def top_lyrics(top_lyrics):
        artist_top_lyrics = []
        for x in range(len(top_lyrics)):
            artist_top_lyrics.append(top_lyrics[x])
        return artist_top_lyrics

class Albums(object):
    def albums(albums):
        artist_albums = []
        for x in range(len(albums)):
            artist_albums.append(albums[x])
        return artist_albums
