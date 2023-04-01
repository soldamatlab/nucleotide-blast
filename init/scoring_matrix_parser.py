import csv

DEFAULT_DELIMITER = ','

def parse_scoring_matrix(path, delimiter=DEFAULT_DELIMITER):
    """
    Parses a scoring matrix from a .csv file saved in [path] to a 2D dictionary (a dictionary of dictionaries).

    :return scoring_matrix: dictionary[str]{ dictionary[str]{ int } }
    """
    if delimiter is None:
        delimiter = DEFAULT_DELIMITER

    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        #reader = csv.DictReader(csvfile, delimiter=delimiter)

        scoring_matrix = {}
        column_keys = next(reader)[1:] # [1:] skips the name of the first column with row labels
        for row in reader:
            row_dict = {}
            for i in range(len(row))[1:]:
                row_dict[column_keys[i-1]] = int(row[i])
            scoring_matrix[row[0]] = row_dict

    return scoring_matrix
