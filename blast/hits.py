def preproc_sequence(sequence): return sequence.upper()

def find_hits_in_database(seeds, database, k):
    """
    :param seeds:
    :param database:
    :param k:

    :return database_hits:  hits of given seeds in the database, list of lists (one for each file in database) of tuples
                            (one for each hit) of shape ([seed], [position in file])
    """
    database_hits = []
    for data in database:
        database_hits.append(find_hits(seeds, data, k))
    return database_hits

def find_hits(seeds, sequence, k):
    sequence = preproc_sequence(sequence)
    hits = []
    for i in range(len(sequence) - k + 1):
        for seed in seeds:
            if sequence[i:i+k].seq == seed:
                hits.append((seed, i))
    return hits
