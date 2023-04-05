BEST_SCORE_CUTOFF = 0.1


def print_results(database, matches, blast_time):
    print_matches(database, matches)
    print("\nBLAST found %d matches in " %
          len(matches) + format_elapsed_time(blast_time))


def print_matches(database, matches):
    print("\n__________ Found matches: __________")

    best_score = matches[-1][3]
    for match in matches:
        if match[3] < best_score * BEST_SCORE_CUTOFF:
            continue
        print("match:   file \"" +
              database[match[2]].id +
              "\" " +
              format_range(match[1]) +
              " <=> " +
              format_range(match[0]) +
              " query   score = %d" % match[3])


def format_range(range):
    return "[" + str(range[0]+1) + ", " + str(range[1]+1) + "]"


def format_elapsed_time(elapsed_time):
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    return time_piece(hours, "hours") + time_piece(minutes, "minutes") + "%f seconds" % seconds


def time_piece(time, name): return "%d " % time + name + ", " if time else ""        
