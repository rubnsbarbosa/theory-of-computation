class Transition:
    def __init__(self, origin, symbol, destiny):
        self.origin = origin
        self.symbol = symbol
        self.destiny = destiny

    def __str__(self):
        return '\tS({},{}) => {}'.format(self.origin, self.symbol, self.destiny)