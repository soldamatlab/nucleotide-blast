from init.input import load_input
from blast import blast

if __name__ == '__main__':
    sequence, database, k, t, S = load_input()

    blast(sequence, database, k, t, S)
