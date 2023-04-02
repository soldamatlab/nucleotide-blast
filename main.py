from time import time

from lib.init.input import load_input
from lib.blast.blast import blast
from lib.output.results import print_results

if __name__ == '__main__':
    sequence, database, k, t, S = load_input()

    blast_start = time()
    matches = blast(sequence, database, k, t, S)
    finished = time()
    
    print_results(database, matches, finished-blast_start)

