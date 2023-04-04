from lib.blast.automaton import create_hit_detection_automaton


# vars for info prints
PRINT_SPEED = 1000000  # one print per [PRINT_SPEED] symbols searched
file_number = [0]
n_files = [0]


def find_hits_in_database(seeds, database, k, alphabet):
    """
    :param seeds:
    :param database:
    :param k:

    :return database_hits:  hits of given seeds in the database, list of lists (one for each file in database) of tuples
                            (one for each hit) of shape ([seed], [position in file])
    """
    print_initial(len(database))
    
    automaton = create_hit_detection_automaton(seeds, k, alphabet)
    database_hits = []
    for d in range(len(database)):
        print_file_initial(d+1, database[d].id)
        # database_hits.append(find_hits(seeds, data, k))
        database_hits.append(find_hits_automaton(database[d], k, automaton))

    print_finish(sum([len(file_hits) for file_hits in database_hits]))
    return database_hits


def find_hits(seeds, sequence, k):
    # vars for print_file_progress
    X = 0
    N = len(sequence)

    hits = []
    for s in range(len(sequence) - k + 1):
        for seed in seeds:
            if sequence[s:s+k].seq == seed:
                hits.append((seed, s))
        X = print_file_progress(s, X, N)
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
        X = print_file_progress(s, X, N)
    return hits


# Info prints:
def print_initial(number_of_files):
    print("Searching for seed hits in database.")
    n_files[0] = number_of_files


def print_file_initial(file_num, file_id):
    file_number[0] = file_num
    print("Searching for seed hits in file [%d/%d]: " %
          (file_number[0], n_files[0]) + file_id)


def print_file_progress(s, X, N):
    if not (s+1) % PRINT_SPEED:
        X = X + PRINT_SPEED
        print("Searching file [%d/%d]: %d/%d (%f%%)" %
              (file_number[0], n_files[0], X, N, 100*X/N))
    return X


def print_finish(n_hits):
    print("%d total hits found." % n_hits)
