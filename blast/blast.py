from blast.seeds import get_seeds
from blast.hits import find_hits_in_database

def blast(sequence, database, k, t, S):
    """
    :param k: length of the word
    :param t: scoring threshold
    :param S: scoring matrix
    """
    seeds, seed_positions = get_seeds(sequence, k, t, S)
    database_hits = find_hits_in_database(seeds, database, k)

    print("sequence:")
    print(sequence)
    print("seeds:")
    print(seeds)
    print("seed_positions:")
    print(seed_positions)
    print("database:")
    print(database)
    print("database_hits:")
    print(database_hits)

    return 0
