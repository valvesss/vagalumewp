class Song(object):
    def __init__(self, song):
        self.id = song['id']
        self.lang = song['lang']
        self.name = song['name']
        self.text = song['text']
        self.url = song['url']

class Artist(object):
    def __init__(self, artist):
        self.id = artist['id']
        self.name = artist['desc']
        self.url = artist['url']
        self.pic_small = artist['pic_small']
        self.pic_medium = artist['pic_medium']
        self.rank = Rank.rank(artist['rank'])
        self.top_lyrics = Toplyrics.top_lyrics(artist['toplyrics']['item'])
        self.albums = Albums.albums(artist['albums']['item'])
        self.genre = Genre.genre(artist['genre'])
        self.related = Related.related(artist['related'])

class Rank(object):
    def rank(rank):
        return {key: value for key, value in rank.items()}

class Genre(object):
    def genre(genre):
        return [genre[x] for x in range(len(genre))]

class Related(object):
    def related(related):
        return [related[x] for x in range(len(related))]


class Toplyrics(object):
    def top_lyrics(top_lyrics):
        return [top_lyrics[x] for x in range(len(top_lyrics))]

class Albums(object):
    def albums(albums):
        return [albums[x] for x in range(len(albums))]
