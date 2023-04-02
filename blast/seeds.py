from blast.hits import preproc_sequence

NO_SYMBOL = ' '

seed = []
seeds = []
seed_positions = {}

def get_seeds(sequence, k, t, S):
    """
    :param sequence: query sequence
    :param k:
    :param t:
    :param S:

    :return seeds: found seeds, list of strings of length k
    :return seed_positions: positions of the found seeds in the query sequence, dictionary
                            of lists of positions in sequence (one seed can have multiple
                            positions in query sequence) indexed by found seeds
    """
    sequence = preproc_sequence(sequence)
    pure_seeds = get_pure_seeds(sequence, k, t, S)
    add_unpure_seeds(pure_seeds, k, t, S)
    return seeds, seed_positions

def get_pure_seeds(sequence, k, t, S):
    pure_seeds = []
    for start in range(len(sequence) - k + 1):
        seed = str()
        score = 0
        for symbol_idx in range(k):
            seed += sequence[start + symbol_idx]
            score += S[seed[-1]][seed[-1]]
        if (score >= t):
            if (seed not in pure_seeds):
                pure_seeds.append(seed)
                seed_positions[seed] = [start]
            else:
                seed_positions[seed].append(start)
    return pure_seeds

def add_unpure_seeds(pure_seeds, k, t, S):
    for i in range(k): seed.append(NO_SYMBOL)
    for pure_seed in pure_seeds:
        recurent_seed_score(pure_seed, 0, k, 0, S, t)

def recurent_seed_score(pure_seed, pos, k, score, S, t):
    if pos == k:
        if score >= t:
            new_seed = "".join([str(i) for i in seed])
            if new_seed not in seeds:
                seeds.append(new_seed)
                seed_positions[new_seed] = seed_positions[pure_seed]
        return
    
    for symbol in get_alphabet(S):
        seed[pos] = symbol
        recurent_seed_score(pure_seed, pos+1, k, score+S[pure_seed[pos]][symbol], S, t)


def get_alphabet(S): return list(S.keys())
