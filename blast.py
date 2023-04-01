import numpy as np

def blast(sequence, database, k, t, S):
    """
    :param k: length of the word
    :param t: scoring threshold
    :param S: scoring matrix
    """
    sequence = preproc_sequence(sequence)

    seeds = get_seeds(sequence, k, t, S)
    database_hits = find_hits_in_database(seeds, database, k)

    print("sequence:")
    print(sequence)
    print("seeds:")
    print(seeds)
    print("database:")
    print(database)
    print("database_hits:")
    print(database_hits)

    return 0

def preproc_sequence(sequence): return sequence.upper()

def get_seeds(sequence, k, t, S):
    seeds = get_pure_seeds(sequence, k, t, S)
    seeds = add_unpure_seeds(seeds, k, t, S)
    return seeds

def get_pure_seeds(sequence, k, t, S):
    seeds = []
    for start in range(len(sequence) - k + 1):
        seed = str()
        score = 0
        for symbol_idx in range(k):
            seed += sequence[start + symbol_idx]
            score += S[seed[-1]][seed[-1]]
        if (score > t) & (seed not in seeds):
            seeds.append(seed)
    return seeds

def add_unpure_seeds(seeds, k, t, S):
    # TODO
    return seeds

def find_hits_in_database(seeds, database, k):
    database_hits = []
    for i in range(len(database)):
        database_hits.append(find_hits(seeds, database[i], k))
    return database_hits

def find_hits(seeds, sequence, k):
    sequence = preproc_sequence(sequence)
    hits = []
    for i in range(len(sequence) - k + 1):
        for seed in seeds:
            if sequence[i:i+k].seq == seed: # TODO ? cast .seq to string
                hits.append(i)
    return hits