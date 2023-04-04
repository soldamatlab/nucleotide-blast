SCORE_DECREASE_CUTOFF = 0


def extend_hits(database, hits, k, seed_positions, sequence, S):
    """
    :return matches:    list of lists (one or each file in database) of tuples (one for each hit)
                        of shape (seqeunce_range, file_range, score)
    """
    print("Extending seed hits into gapless matches.")
    # TODO extend best seed hit first, or rather cut off unnecessary unpure seed hits in hits.py
    matches = []
    for file_idx in range(len(database)):
        file_symbols_matched = len(database[file_idx]) * [False]
        for hit in hits[file_idx]:
            if file_symbols_matched[hit[1]]:
                continue
            for sequence_position in seed_positions[hit[0]]:
                sequence_range, file_range, score = gapless_extend(
                    database[file_idx], hit[1], k, sequence, sequence_position, S)
                file_symbols_matched[file_range[0]: file_range[1]] = \
                    (file_range[1] - file_range[0]) * [True]
                matches.append((sequence_range, file_range, file_idx, score))
    return matches


def gapless_extend(file, file_position, k, sequence, sequence_position, S):
    """
    :param file: single file from database
    :param file_position: position of hit in file, int
    :param k:
    :param sequence:
    :param sequence_position:
    """
    left_extension, left_score = one_sided_gapless_extend(
        file, file_position, sequence, sequence_position, False, S)
    right_extension, right_score = one_sided_gapless_extend(
        file, file_position+k-1, sequence, sequence_position+k-1, True, S)

    sequence_range = (sequence_position - left_extension,
                      sequence_position + k-1 + right_extension)
    file_range = (file_position - left_extension,
                  file_position + k-1 + right_extension)
    score = left_score + right_score + \
        hit_score(file, file_position, k, sequence, sequence_position, S)
    return sequence_range, file_range, score


def one_sided_gapless_extend(file, file_pos, sequence, sequence_pos, go_right, S):
    if go_right:
        seq_idx_range = range(sequence_pos+1, len(sequence))
        file_idx_bound = len(file) - 1
        bool_sign = 1
    else:
        seq_idx_range = range(sequence_pos-1, -1, -1)
        file_idx_bound = 0
        bool_sign = -1

    score = 0
    best_score = score
    best_extenstion = 0
    for i in range(len(seq_idx_range)):
        seq_idx = seq_idx_range[i]
        file_idx = file_pos + (seq_idx - sequence_pos)
        if (bool_sign * file_idx > file_idx_bound):
            break

        score += S[sequence[seq_idx]][file[file_idx]]
        if score > best_score:
            best_score = score
            best_extenstion = i + 1
        elif score < best_score - SCORE_DECREASE_CUTOFF:
            break
    return best_extenstion, best_score


def hit_score(file, file_position, k, sequence, sequence_position, S):
    score = 0
    for i in range(k):
        score += S[sequence[sequence_position + i]][file[file_position + i]]
    return score
