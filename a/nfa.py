# coding: utf-8
import pandas as pd
from state import State
from alphabet import Alphabet
from transition import Transition

class NFA:
    def __init__(self):
        self.states = State()
        self.sigma = Alphabet()
        self.delta = list()
        self.delta_nfa = list()
        self.initial_state = None
        self.final_state = list()

    def add_states(self, states):
        for s in states:
            self.states.add_states(s)

    def add_alphabet(self, symbols):
        for s in symbols:
            self.sigma.add_symbol(s)

    def add_initial_state(self, init_state):
        states = self.states.get_states()
        if init_state in states:
            self.initial_state = init_state
        else:
            print("O estado inicial nao pertence ao conjunto de estados")

    def add_final_state(self, *elements):
        states = self.states.get_states()
        for x in elements:
            if x in states:
                self.final_state.append(x)
            else:
                print("O estado final nao pertence ao conjunto de estados")

    def get_transitions_nfa(self):
        nfa = pd.read_csv("nfa.csv", header=None)
        aux = []

        for i, values in nfa.iteritems():
            self.delta = (nfa[i].values[0:])

        for x in range(len(self.delta)):
            aux = self.delta[x]
            self.delta[x] = self.delta[1:]
                
            origin, symbol, destiny = aux
            self.delta_nfa.append(Transition(origin, symbol, destiny))

    def execute_transition(self, string_w):
        state_origin = self.initial_state
        state_destiny = list()

        for w in string_w:
            for x in range(len(self.delta)):
                if w == self.delta_nfa[x].symbol and (state_origin in self.delta_nfa[x].origin):
                    print(f"origin: {self.delta_nfa[x].origin} - symbol: {self.delta_nfa[x].symbol} - destiny: {self.delta_nfa[x].destiny}")
                    state_destiny = (self.delta_nfa[x].destiny)
                    state_origin = state_destiny

        print(f"A string digitada chegou ao estado final: {state_destiny}")
        if state_destiny in self.final_state:
            print("Aceita")
        else:
            print("Rejeita") 

    def __str__(self):
        print(f"Estado inicial: {self.initial_state}")
        print(f"Estado final: {self.final_state}")

    def __delta__(self):
        print("Função de transição (Q x E) -> Q")
        for x in range(len(self.delta)):
            print(f"origin: {self.delta_nfa[x].origin} - symbol: {self.delta_nfa[x].symbol} - destiny: {self.delta_nfa[x].destiny}")
        