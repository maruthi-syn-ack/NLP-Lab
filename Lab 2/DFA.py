# Author : MARUTHI R (github.com/maruthi-syn-ack)

# Regular Language: Number divisible by 2


class DFA:
    def __init__(self, states, alphabet, transition, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.current_state = start_state
        self.accept_states = accept_states

    def process_input(self, input_string):
        
        for char in input_string:
            if char not in self.alphabet:
                return False  # Reject if the input contains characters not in the alphabet
            self.current_state = self.transition.get((self.current_state, char), None)
            if self.current_state is None:
                return False  # Transition to a dead state

        return self.current_state in self.accept_states


if __name__ == '__main__':
    # Define the 5-tuple for the DFA that accepts binary numbers divisible by 2
    states = {'q0', 'q1'}
    alphabet = {'0', '1'}
    start_state = 'q0'
    accept_states = {'q0'}

    # Define the transition function as a dictionary
    transition = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q0',
        ('q1', '1'): 'q1',
    }

    # Create a DFA instance
    dfa = DFA(states, alphabet, transition, start_state, accept_states)

    # Get the input string from the user
    input_string = input("Enter a binary number: ")

    # Run the automaton and print the result
    result = dfa.process_input(input_string)
    if result:
        print("Accepted")
    else:
        print("Rejected")