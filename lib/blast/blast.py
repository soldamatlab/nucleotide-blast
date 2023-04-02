from lib.blast.seeds import get_seeds
from lib.blast.hits import find_hits_in_database
from lib.blast.extension import extend_hits


def blast(sequence, database, k, t, S):
    """
    :param sequence:
    :param database:
    :param k: length of the word
    :param t: scoring threshold
    :param S: scoring matrix

    :return matches:    list of lists (one or each file in database) of tuples (one for each hit)
                        of shape (seqeunce_range, file_range)
    """
    print("BLAST started.")

    print("Searching for seeds in query sequence.")
    seeds, seed_positions = get_seeds(sequence, k, t, S)
    print("%d unique seeds found with %d viable \"seed & position in query sequence\" combinations." %
          (len(seeds), sum([len(positions) for positions in seed_positions])))

    print("Searching for seed hits in database.")
    hits = find_hits_in_database(seeds, database, k)
    print("%d total hits found." % sum([len(file_hits) for file_hits in hits]))

    print("Performing gapless extension of the hits.")
    matches = extend_hits(database, hits, k, seed_positions, sequence, S)

    print("BLAST finished.")
    return matches
