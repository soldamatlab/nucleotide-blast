import argparse
from init.scoring_matrix_parser import DEFAULT_DELIMITER

def init_parser():
    parser = argparse.ArgumentParser()

    # arguments from the assignment:
    parser.add_argument("--scoring_matrix", "-e", help="path to the score matrix in CSV format", required=True, type=str)
    #parser.add_argument("-p", help="gap penalization")
    #parser.add_argument("-x", help="gap extension penalization")
    parser.add_argument("--database", "-d", help="list of database files in fasta format", nargs="+", required=True, type=str)
    parser.add_argument("--word_length", "-k", help="length of the word", required=True, type=int)
    parser.add_argument("--threshold", "-t", help="scoring threshold", required=True, type=int)

    # aruments added by me:
    parser.add_argument("--sequence", "-q", help="query sequence", type=str)
    parser.add_argument("--delimiter", help="Specifies delimiter of the score matrix in CSV format. Default delimiter is '" + DEFAULT_DELIMITER + "'. (Common delimiters like ',' or ';' have to be passed with quotation marks.)", type=str)

    args = parser.parse_args()
    return args, parser
