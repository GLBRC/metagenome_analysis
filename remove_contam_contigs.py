#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove contigs marked as contaminated using combining_contig_evals.py script

Read in FASTA and corresponding contigs_to_remove.txt file, match, keep only contigs
not present in the contigs_to_remove.txt file

Created on Wed Mar  4 13:52:35 2020

@author: kevinmyers
"""
from Bio import SeqIO
import os

all_files = []

all_files = [ fn for fn in os.listdir(os.getcwd()) if fn.endswith("contigs_to_remove.txt") ]

bins = []
for each in all_files:
    binID = each.split("_contigs")[0]
    if binID in bins:
        pass
    else:
        bins.append(binID)
        
for IDbins in bins:
    contigs = []
    
    with open(IDbins + '_contigs_to_remove.txt', 'r') as f:
        next(f)
        next(f)
        next(f)
        for line in f:
            name = line.split('\t')[0]
            contigs.append(name)
            
    output = []
    for seq_record in SeqIO.parse(IDbins + '.fasta', 'fasta'):
        if seq_record.id not in contigs:
            output.append(f">{seq_record.id}\n{seq_record.seq}\n")
        else:
            pass
        
    for each in output:
        with open(IDbins + '_cleaned.fasta', 'a') as f:
            f.write(each)