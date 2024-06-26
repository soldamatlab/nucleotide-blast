automaton = {}


def create_hit_detection_automaton(seeds, k, alphabet):
    recursive_automaton_creation("", seeds, k, alphabet)
    return automaton


def recursive_automaton_creation(state, seeds, k, alphabet):
    if len(state) == k+1:
        return

    automaton[state] = {}
    for symbol in alphabet:
        automaton[state][symbol] = find_next_state(state+symbol, seeds, k)
        if len(automaton[state][symbol]) == len(state) + 1:
            recursive_automaton_creation(state+symbol, seeds, k, alphabet)


def find_next_state(state, seeds, k):
    if len(state) == k+1:
        return find_best_substate(state, seeds, start_lb=1)

    for seed in seeds:
        for c in range(len(state)):
            if state[c] != seed[c]:
                break
        else:
            return state
    return find_best_substate(state, seeds)


def find_best_substate(state, seeds, start_lb=0):
    for start in range(start_lb, len(state)):
        for seed in seeds:
            for c in range(start, len(state)):
                if state[c] != seed[c-start]:
                    break
            else:
                return state[start:]
    return ""
