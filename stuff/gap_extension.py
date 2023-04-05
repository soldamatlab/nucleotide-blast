import math
import numpy as np

from lib.blast.extension import compute_sdc

SCORE_DECREASE_MULTIPLIER = 3
GAP_ENABLE = 1
GAP_ENABLE_LOG_BASE = 10


def extend_matches(database, matches, sequence, S, gap_penalization):
    score_decrease_cutoff = compute_sdc(S)\
        + compute_gap_enable(len(sequence), gap_penalization)
    for match in matches:
        extend_match(
            match, sequence, database[match[2]], S, gap_penalization, score_decrease_cutoff)


def extend_match(match, sequence, file, S, gap_penalization, score_decrease_cutoff):
    sequence_range = match[0]
    file_range = match[1]
    file_idx = match[2]
    score = match[3]

    best_score = 0
    best_end = (0, 0)
    D = init_score_matrix()
    for f in range(file_range[1]+1, len(file)):
        active = False
        for s in range(sequence_range[1]+1, len(sequence)):
            d1 = f - file_range[1]
            d2 = s - sequence_range[1]

            substitute = D[d1-1][d2-1] + S[file[f]][sequence[s]]
            if d2 == 1:
                gap_file = float('inf')
            else:
                gap_file = D[d1][d2-1] - gap_penalization
            if d1 == 1:
                gap_sequence = float('inf')
            else:
                gap_sequence = D[d1-1][d2] - gap_penalization
            D[d1][d2] = max([substitute, gap_file, gap_sequence])

            if D[d1][d2] < best_score - score_decrease_cutoff:
                D[d1][d2] = float('inf')
            else:
                active = True
                if D[d1][d2] > best_score:
                    best_score = D[d1][d2]
                    best_end = (d1, d2)
        if not active:
            break
    return best_end, best_score


def init_score_matrix(file, file_range, sequence, sequence_range, gap_penalization):
    D = np.zeros([len(file) - file_range[1],
                 len(sequence) - sequence_range[1]])
    for f in range(D.shape[0]):
        D[f][0] = f * gap_penalization
    for s in range(D.shape[1]):
        D[0][s] = f * gap_penalization


def compute_gap_enable(sequence_length, gap_penalization):
    n_gaps = GAP_ENABLE + int(math.log(sequence_length, GAP_ENABLE_LOG_BASE))
    return n_gaps * gap_penalization
