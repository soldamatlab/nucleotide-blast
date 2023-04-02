from lib.init.arg_parser import init_parser
from lib.init.scoring_matrix_parser import parse_scoring_matrix
from lib.init.fasta_reader import read_fasta_files

def load_input():
    args, parser = init_parser()
    k = args.word_length
    t = args.threshold
    S = parse_scoring_matrix(args.scoring_matrix, args.delimiter)
    database = read_fasta_files(args.database)

    sequence = args.sequence
    if sequence == None:
        sequence = input("Input the query sequence:")

    return sequence, database, k, t, S
