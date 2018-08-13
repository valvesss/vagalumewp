from pprint import pprint

class Artist():
    def __init__(self, artist):
        self.id = artist['id']
        self.name = artist['desc']
        self.url = artist['url']
        self.pic_small = artist['pic_small']
        self.pic_medium = artist['pic_medium']
        self.rank = Rank.Rank(artist['rank'])
        self.genre = Genre.Genre(artist['genre'])
        # self.related = Related(artist['related'])
        self.top_lyrics = Toplyrics(['toplyrics'])
        self.albums = Albums(artist['albums']['item'])

    def get_rank(self):
        return self.rank

    def get_genre(self):
        return self.genre


class Rank():

    def Rank(rank):
        all_rank = {}
        for key, value in rank.items():
            all_rank[key] = value
        return all_rank

class Genre():

    def Genre(genre):
        all_genres = {}
        for item in genre:
            all_genres[item['name']] = item['url']
        return all_genres

# class Related(list):
#
#     def Related(related):
#         all_relateds = {}
#         for item in related:
#             all_relateds
#         self.all_relates.append(related['id'], related['name'], related['url'])

class Toplyrics(list):

    def add_toplyrics(self, toplyrics):
        self.all_top_lyrics = []
        self.all_top_lyrics.append(toplyrics['id'], toplyrics['desc'], toplyrics['url'])

class Albums(list):

    def add_album(self, albums):
        self.all_albums = []
        self.all_albums.append(album['id'], album['desc'], album['url'], album['year'], album['label'])
