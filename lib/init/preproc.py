def preproc_sequence(sequence): return sequence.upper()


def preproc_database(database):
    for i in range(len(database)):
        database[i] = preproc_sequence(database[i])
    return database
