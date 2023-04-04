from lib.blast.seeds import get_seeds
from lib.blast.hits import find_hits_in_database
from lib.blast.extension import extend_hits
from lib.blast.match_sort import sort_matches


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
    seeds, seed_positions = get_seeds(sequence, k, t, S)
    hits = find_hits_in_database(seeds, database, k, list(S.keys()))
    matches = extend_hits(database, hits, k, seed_positions, sequence, S)
    matches = sort_matches(matches)
    print("BLAST finished.")
    return matches
