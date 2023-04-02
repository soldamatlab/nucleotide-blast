from lib.init.input import load_input
from lib.blast.blast import blast

if __name__ == '__main__':
    sequence, database, k, t, S = load_input()
    matches = blast(sequence, database, k, t, S)
    #print_results(matches)

