class Alphabet:
    def __init__(self):
        self.symbols = list()

    def add_symbol(self, s):
        self.symbols.append(s)

    def print_symbols(self):
        print("symbols: {}".format(self.symbols))
