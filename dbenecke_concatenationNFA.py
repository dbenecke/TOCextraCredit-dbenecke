import csv

def load_nfa_csv(filename):
    #open csv file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    #get nfa structure
    nfa = {
        'states': rows[0], #states
        'alphabet': rows[1], #alphabet
        'start': rows[2][0], #start state
        'accept': rows[3], #accept states
        'transitions': [] #empty list for transitions
    }

    #add transitions
    for row in rows[4:]:
        nfa['transitions'].append({'from': row[0], 'input': row[1], 'to': row[2]})

    return nfa


def save_nfa_csv(filename, nfa):
    #open csv file to write on it the new info
    with open(filename, 'w') as file:
        #write states, alphabet, start state, and accept states
        file.write(','.join(nfa['states']) + '\n')
        file.write(','.join(nfa['alphabet']) + '\n')
        file.write(nfa['start'] + '\n')
        file.write(','.join(nfa['accept']) + '\n')

        #write transitions
        for transition in nfa['transitions']:
            file.write(f"{transition['from']},{transition['input']},{transition['to']}\n")


def concatenate_nfa(nfa1, nfa2):
    #create a new NFA for the result
    concatenated = {
        'states': nfa1['states'] + nfa2['states'], #combine states
        'alphabet': list(set(nfa1['alphabet'] + nfa2['alphabet'])), #combine alphabets
        'start': nfa1['start'], #start state is the same as NFA1's start
        'accept': nfa2['accept'], #accept states come from NFA2
        'transitions': nfa1['transitions'] + nfa2['transitions'] #combine transitions
    }

    #add epsilon transitions from NFA1's accept states to NFA2's start state
    for accept_state in nfa1['accept']:
        concatenated['transitions'].append({'from': accept_state, 'input': 'e', 'to': nfa2['start']})

    return concatenated


def display_nfa(nfa):
    #print information for the new nfa
    print("States:", ", ".join(nfa['states']))
    print("Alphabet:", ", ".join(nfa['alphabet']))
    print("Start State:", nfa['start'])
    print("Accept States:", ", ".join(nfa['accept']))
    print("Transitions:")
    for transition in nfa['transitions']:
        print(f"  {transition['from']} --{transition['input']}--> {transition['to']}")


if __name__ == "__main__":
    #input files for NFAs
    nfa1_file = 'dbenecke_nfa1.csv'
    nfa2_file = 'dbenecke_nfa2.csv'

    #load NFAs
    nfa1 = load_nfa_csv(nfa1_file)
    nfa2 = load_nfa_csv(nfa2_file)

    #concatenate the two NFAs
    concatenated_nfa = concatenate_nfa(nfa1, nfa2)

    #save the concatenated NFA to a new file
    concatenated_nfa_file = 'dbenecke_concatenated_nfa_output.csv'
    save_nfa_csv(concatenated_nfa_file, concatenated_nfa)

    #show concatenated NFA
    display_nfa(concatenated_nfa)
