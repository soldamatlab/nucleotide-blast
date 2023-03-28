from Bio import SeqIO

def read_fasta_files(paths):
    for path in paths:
        for record in SeqIO.parse(path, "fasta"):
            print(record.id)

    return [] # TODO
