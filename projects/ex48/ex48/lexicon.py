class Lexicon(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def scan (self, direction):
        return self.paths.get(direction, None)
