# coding: utf-8
from nfa import NFA
from state import State

if __name__ == "__main__":
    
    """ Criando um NFA. """
    automaton = NFA()

    """ Adicionando os estatos no automato. """
    automaton.add_states("ABC")
    automaton.states.print_states()

    """ Adicionando o alfabeto ou conjunto de simbolos. """
    automaton.add_alphabet("01")    
    automaton.sigma.print_symbols()

    """ Adicionando o estado inicial. """
    automaton.add_initial_state("A")

    """ Adicionando o(s) estado(s) final(is) ou de aceitacao. """
    # automaton.add_final_state("B","C")
    automaton.add_final_state("C")
    automaton.__str__()

    """ Pegando as transições dos estados do NFA no arquivo CSV """
    automaton.get_transitions_nfa()
    automaton.__delta__()
    print("\n")

    """ funcao de transicao """
    string_word = input("Digite uma sequencia de símbolos: ")
    automaton.execute_transition(string_word)