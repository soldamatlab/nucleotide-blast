import numpy as np

NO_SYMBOL = ' '

seed = []
seeds = []

def get_seeds(sequence, k, t, S):
    pure_seeds = get_pure_seeds(sequence, k, t, S)
    add_unpure_seeds(pure_seeds, k, t, S)
    return seeds

def get_pure_seeds(sequence, k, t, S):
    pure_seeds = []
    for start in range(len(sequence) - k + 1):
        seed = str()
        score = 0
        for symbol_idx in range(k):
            seed += sequence[start + symbol_idx]
            score += S[seed[-1]][seed[-1]]
        if (score >= t) & (seed not in pure_seeds):
            pure_seeds.append(seed)
    return pure_seeds

def add_unpure_seeds(pure_seeds, k, t, S):
    for i in range(k): seed.append(NO_SYMBOL)
    for pure_seed in pure_seeds:
        recurent_seed_score(pure_seed, 0, k, 0, S, t)

def recurent_seed_score(pure_seed, pos, k, score, S, t):
    if pos == 0:
        print(score)
    if pos == k:
        if score >= t:
            new_seed = "".join([str(i) for i in seed])
            if new_seed not in seeds:
                seeds.append(new_seed)
        return
    
    for symbol in get_alphabet(S):
        seed[pos] = symbol
        recurent_seed_score(pure_seed, pos+1, k, score+S[pure_seed[pos]][symbol], S, t)


def get_alphabet(S): return list(S.keys())
