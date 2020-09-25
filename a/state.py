class State:
    def __init__(self):
        self.state = list()
        
    def add_states(self, s):
        self.state.append(s)

    def get_states(self):
        return self.state

    def print_states(self):
        print("Estados: {}".format(self.state))