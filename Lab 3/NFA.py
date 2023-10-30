def Set_states():
    nfa = {
    'states': set(),
    'alphabet': set(),
    'transitions': {},
    'start_state': None,
    'accept_states': set()
    }


    # Input states
    states_input = input("Enter states (comma-separated): ")
    nfa['states'] = set(states_input.split(','))
    
    # Input alphabet
    alphabet_input = input("Enter alphabet symbols (comma-separated): ")
    nfa['alphabet'] = set(alphabet_input.split(','))
    
    # Input transitions
    print("Enter transitions (Enter 'done' when finished):")
    while True:
        state = input("From state (Enter 'done' to stop): ")
        if state == 'done':
            break
        symbol = input("On symbol: ")
        to_states_input = input("To states (comma-separated): ")
        to_states = set(to_states_input.split(','))
        if state not in nfa['transitions']:
            nfa['transitions'][state] = {}
        nfa['transitions'][state][symbol] = to_states
    # Input initial state
    start_state = input("Enter initial state: ")
    nfa['start_state'] = start_state
    # Input accepting states
    accept_states_input = input("Enter accepting states (comma-separated): ")
    nfa['accept_states'] = set(accept_states_input.split(','))
    return nfa
    
def Process_NFA_bfs(nfa, input_string):
    

    from collections import deque 
    """
    Run the NFA on the given input string and check if it's accepted or not using BFS.
    """
    current_states = {nfa['start_state']}
    queue = deque()
    queue.append(current_states)
    
    print(f"Start state: {current_states}")

    for symbol in input_string:
        if symbol not in nfa['alphabet']:
            print(f"Invalid symbol: {symbol}")
            return False  # Invalid symbol

        next_states = set()

        for state in current_states:
            next_states.update(nfa['transitions'][state].get(symbol, set()))

        if not next_states:
            print(f"No transition from states {current_states} with symbol {symbol}")
            return False

        print("--------------------------------------------------------------------------------------")
        print(f"Transition from states {current_states} to states {next_states} with symbol {symbol}")
        print("--------------------------------------------------------------------------------------")
        
        queue.append(next_states)
        current_states = next_states

    # Continue BFS until the end of the input string
    while queue:
        current_states = queue.popleft()

    return any(state in nfa['accept_states'] for state in current_states)


if __name__ == "__main__":
    ch=0
    while ch!=3: 
        print("-----------------------------------------------------------------------------------------")
        print(" 1.Create a new NFA state Instance \n 2. Validate Strings With already created NFA \n 3. Exit()")
        print("\n\n")
        ch = int(input())
        if(ch == 1):
            ch=0
            nfa = Set_states()
        elif(ch == 2):
            ch=0
            # Input the string
            input_string = input("Enter a string (0s and 1s only): ")
        
            # Check the validity
            print("String Validatin by NFA using BFS.")
            
            if Process_NFA_bfs(nfa, input_string):
                print("String is valid and accepted by the NFA.")
            else:
                print("String is invalid and not accepted by the NFA.")
            
    print("Exiting Program")
