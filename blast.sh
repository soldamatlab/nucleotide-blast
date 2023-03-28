#!/bin/bash
python main.py -e ./data\scoring_matrix\blosum62.csv -d ./data\database\Homo_sapiens.GRCh38.dna_sm.chromosome.16.fa -k 5 -t 20 --delimiter ';'
