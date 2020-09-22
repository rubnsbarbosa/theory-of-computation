# coding: utf-8
from dfa import DFA
from state import State


if __name__ == "__main__":
    
    """ Criando um DFA. """
    automaton = DFA()

    """ Criando os estatos: A, B e C. """
    a = State("A")
    b = State("B")
    c = State("C")
    
    """ Adicionando os estatos no automato. """
    automaton.add_states(a)
    automaton.add_states(b)
    automaton.add_states(c)    
    
    """ Criando listas de adjacencias entre os estatos. """
    a.add_neighbor("A")
    a.add_neighbor("B")
    b.add_neighbor("B")
    b.add_neighbor("C")
    c.add_neighbor("C")
    automaton.print_dfa()

    """ Adicionando o alfabeto ou conjunto de simbolos. """
    automaton.add_alphabet("01")    
    automaton.sigma.print_symbols()

    """ Adicionando o estado inicial. """
    automaton.add_initial_state("A")

    """ Adicionando o(s) estado(s) final(is) ou de aceitacao. """
    # automaton.add_final_state("B","C")
    automaton.add_final_state("C")
    
    """ Adicionando as transicoes dos estados. """
    # B A B C C C  [1000 - rejeita] - [101 - aceita]
    automaton.add_transitions()
    automaton.__str__()
    print("\n")
    
    """ funcao de transicao """
    string_word = input("Digite uma sequencia de símbolos: ")
    automaton.execute_transition(string_word)
