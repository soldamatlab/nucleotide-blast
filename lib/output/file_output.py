from lib.output.results import *


def print_into_file(database, matches, blast_time):
    with open('blast_output.txt', 'w') as f:
        print("BLAST found %d matches in " %
              len(matches) + format_elapsed_time(blast_time), file=f)
        print("\n__________ Found matches: __________", file=f)
        for m in range(len(matches)-1, -1, -1):
            print("match:   file \"" +
                database[matches[m][2]].id +
                "\" " +
                format_range(matches[m][1]) +
                " <=> " +
                format_range(matches[m][0]) +
                " query   score = %d" % matches[m][3],
                file=f)
