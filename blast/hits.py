def preproc_sequence(sequence): return sequence.upper()

def find_hits_in_database(seeds, database, k):
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
                hits.append(i)
    return hits
