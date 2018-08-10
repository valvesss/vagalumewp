class Artist():
    def __init__(self, artist):
        self.id = artist['id']
        self.name = artist['desc']
        self.url = artist['url']
        self.picsmall = artist['pic_small']
        self.medium = artist['pic_medium']

class Rank():
    def __init__(self, rank):
        self.pos = rank['pos']
        self.period = rank['period']
        self.views = rank['views']
        self.uniques = rank['uniques']
        self.points = rank['points']

class Genre():
    def __init__(self, genre):
        self.name = genre['name']
        self.url = genre['url']

class Related():
    def __init__(self, related):
        self.id = related['id']
        self.name = related['name']
        self.url = related['url']
        
class Toplyrics():
    def __init__(self, toplyrics):
        self.id = toplyrics['id']
        self.desc = toplyrics['desc']
        self.url = toplyrics['url']

class Albums():
    def __init__(self, album):
        self.id = album['id']
        self.desc = album['desc']
        self.url = album['url']
        self.year = album['year']
        self.label = album['label']
