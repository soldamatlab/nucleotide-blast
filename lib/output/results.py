def print_results(database, matches, blast_time):
    print_matches(database, matches)
    print("\nBLAST found %d matches in " %
          len(matches) + format_elapsed_time(blast_time))


#def print_matches(database, matches):
#    print("\n__________ Found matches: __________")
#    for file_idx in range(len(database)):
#        print("File name: " + database[file_idx].id)
#
#        for match in matches[file_idx]:
#            print("---match:   file " +
#                  format_range(match[1]) +
#                  " <=> " +
#                  format_range(match[0]) +
#                  " query   score = %d" % match[3])
            

def print_matches(database, matches):
    print("\n__________ Found matches: __________")

    for match in matches:
        print("---match:   file \"" +
                database[match[2]].id +
                "\" " +
                format_range(match[1]) +
                " <=> " +
                format_range(match[0]) +
                " query   score = %d" % match[3])


def format_range(range):
    return "[" + str(range[0]) + ", " + str(range[1]) + "]"


def format_elapsed_time(elapsed_time):
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    return time_piece(hours, "hours") + time_piece(minutes, "minutes") + "%f seconds" % seconds


def time_piece(time, name): return "%d " % time + name + ", " if time else ""
