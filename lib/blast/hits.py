from lib.blast.automaton import create_hit_detection_automaton


PRINT_SPEED = 1000000 # one print per [PRINT_SPEED] symbols searched


def find_hits_in_database(seeds, database, k, alphabet):
    """
    :param seeds:
    :param database:
    :param k:

    :return database_hits:  hits of given seeds in the database, list of lists (one for each file in database) of tuples
                            (one for each hit) of shape ([seed], [position in file])
    """
    automaton = create_hit_detection_automaton(seeds, k, alphabet)
    database_hits = []
    for d in range(len(database)):
        print("Searching file [%d/%d]: " % (d+1, len(database)) + database[d].id)
        #database_hits.append(find_hits(seeds, data, k)) # naive search
        database_hits.append(find_hits_automaton(database[d], k, automaton)) # automaton search
    return database_hits


def find_hits(seeds, sequence, k):
    # vars for print_progress
    X = 0
    N = len(sequence)

    hits = []
    for s in range(len(sequence) - k + 1):
        for seed in seeds:
            if sequence[s:s+k].seq == seed:
                hits.append((seed, s))
        X = print_progress(s, X, N)
    return hits


def find_hits_automaton(sequence, k, automaton):
    # vars for print_progress
    X = 0
    N = len(sequence)

    hits = []
    state = ""    
    for s in range(len(sequence)):
        state = automaton[state][sequence[s]]
        if len(state) == k:
            hits.append((state, s-k+1))
        X = print_progress(s, X, N)
    return hits


def print_progress(s, X, N):
    if not (s+1) % PRINT_SPEED:
        X = X + PRINT_SPEED
        print("Searched %d/%d (%f%%)" % (X, N, 100*X/N))
    return X
