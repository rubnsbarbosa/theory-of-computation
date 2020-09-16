# coding: utf-8
from state import State
from alphabet import Alphabet
from transition import Transition


class DFA:
    def __init__(self):
        self.states = {}
        self.sigma = Alphabet()
        self.delta = list()
        self.initial_state = None
        self.final_state = list()

    def add_states(self, state):
        if isinstance(state, State) and state.name not in self.states:
            self.states[state.name] = state
            return True
        else:
            return False

    def add_alphabet(self, symbols):
        for s in symbols:
            self.sigma.add_symbol(s)

    def add_initial_state(self, init_state):
        if init_state in self.states:
            self.initial_state = init_state
        else:
            print("O estado inicial nao pertence ao conjunto de estados")

    def add_final_state(self, *elements):
        for x in elements:
            if x in self.states:
                self.final_state.append(x)
            else:
                print("O estado final nao pertence ao conjunto de estados")

    def add_transitions(self):
        destiny_state = None
        for i in self.states:
            for j in self.sigma.symbols:
                while(True):
            
                    destiny_state = input(f"Estando no estado: {i} e simbolo: {j}. Qual o seu estado destino? ")

                    if destiny_state in self.states:
                        self.delta.append(Transition(i, j, destiny_state))
                        break
                    else:
                        print("Digite novamente (um estado conhecido)!")
                
        self.delta = self.delta
    
    def execute_transition(self, string_w):
        state_origin = self.initial_state
        state_destiny = list()

        for w in string_w:
            for x in range(len(self.delta)):
                if w == self.delta[x].symbol and (state_origin in self.delta[x].origin):
                    print(f"origin: {self.delta[x].origin} - symbol: {self.delta[x].symbol} - destiny: {self.delta[x].destiny}")
                    state_destiny = (self.delta[x].destiny)
                    state_origin = state_destiny
                    break

        print(f"A string digitada chegou ao estado final: {state_destiny}")
        if state_destiny in self.final_state:
            print("Aceita")
        else:
            print("Rejeita")         


    def __str__(self):
        print(f"\nEstado inicial: {self.initial_state}")
        print(f"Estado final: {self.final_state}")

        print("\nFunção de transição (Q x E) -> Q")

        for x in range(len(self.delta)):
            print(f"origin: {self.delta[x].origin} - symbol: {self.delta[x].symbol} - destiny: {self.delta[x].destiny}")
        
    def print_dfa(self):
        for key in sorted(list(self.states.keys())):
            print(key + str(self.states[key].neighbors))
