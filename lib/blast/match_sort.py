import functools

def sort_matches(matches):
    matches.sort(key=functools.cmp_to_key(compare_matches))
    return matches


def compare_matches(match1, match2):
    if match1[3] < match2[3]:
        return -1
    elif match1[3] > match2[3]:
        return 1
    else:
        return 0
