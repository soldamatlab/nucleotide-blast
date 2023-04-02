from Bio import SeqIO

def read_fasta_files(paths):
    records = []    
    for path in paths:
        for record in SeqIO.parse(path, "fasta"):
            records.append(record)
    return records
