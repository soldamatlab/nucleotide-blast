from arg_parser import init_parser
from scoring_matrix_parser import parse_scoring_matrix
from fasta_reader import read_fasta_files

if __name__ == '__main__':
    args, parser = init_parser()
    S = parse_scoring_matrix(args.scoring_matrix, args.delimiter)
    database = read_fasta_files(args.database)
