from blast.seeds import get_seeds
from blast.hits import find_hits_in_database
from blast.extension import extend_hits

def blast(sequence, database, k, t, S):
    """
    :param k: length of the word
    :param t: scoring threshold
    :param S: scoring matrix
    """
    seeds, seed_positions = get_seeds(sequence, k, t, S)
    hits = find_hits_in_database(seeds, database, k)
    matches = extend_hits(database, hits, k, seed_positions, sequence, S)

    print("sequence:")
    print(sequence)
    print("seeds:")
    print(seeds)
    print("seed_positions:")
    print(seed_positions)
    print("database:")
    print(database)
    print("hits:")
    print(hits)
    print("matches:")
    print(matches)

    return 0
