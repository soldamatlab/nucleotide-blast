from lib.blast.automaton import create_hit_detection_automaton

if __name__ == '__main__':
    seeds = ["abc", "bcd"]
    alphabet = "abcde"
    automaton = create_hit_detection_automaton(seeds, 3, alphabet)
    print(automaton)
