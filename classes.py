class Artist():
    def __init__(self, artist):
        self.id = artist['id']
        self.name = artist['desc']
        self.url = artist['url']
        self.picsmall = artist['pic_small']
        self.medium = artist['pic_medium']
        self.rank = Rank(artist['rank'])
        self.genre = Genre(artist['genre'])
        self.related = Related(artist['related'])
        self.toplyrics = Toplyrics(['toplyrics'])
        self.albums = Albums(artist['albums']['item'])

    def get_genre(self):
        return self.genre

    def get_rank(self):
        return self.rank

class Rank(list):
    def add_rank(self, rank):
        self.rank = []
        self.rank.append(rank['pos'], rank['period'], rank['views'], rank['uniques'], rank['points'])

class Genre(list):

    def add_genre(self, genre):
        self.all_genres = []
        self.all_genres.append(genre['name'], genre['url'])

class Related(list):

    def add_relate(self, related):
        self.all_relates = []
        self.all_relates.append(related['id'], related['name'], related['url'])

class Toplyrics(list):

    def add_toplyrics(self, toplyrics):
        self.all_toplyrics = []
        self.all_toplyrics.append(toplyrics['id'], toplyrics['desc'], toplyrics['url'])

class Albums(list):

    def add_album(self, albums):
        self.all_albums = []
        self.all_albums.append(album['id'], album['desc'], album['url'], album['year'], album['label'])
