#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 14:41:06 2021

Script to organize the contig lengths for passed (cleaned) and removed (contaminated)
contigs into two files. Each line in the file is a contig length.

@author: kevinmyers
"""

import os

cleaned_contigs = []

cleaned_contigs = [ fn for fn in os.listdir(os.getcwd()) if fn.endswith("cleaned_contigs_lengths.txt") ]

bins = []

for each in cleaned_contigs:
    binID = each.split("_cleaned")[0]
    if binID in bins:
        pass
    else:
        bins.append(binID)
        
for IDbins in bins:
    removedLength = []
    with open(IDbins + "_contigs_to_remove.txt", 'r') as f:
        next(f)
        next(f)
        next(f)
        for line in f:
            line = line.rstrip()
            length = line.split('\t')[1]
            removedLength.append(length)
    keepLength = []
    with open(IDbins + "_cleaned_contigs_lengths.txt", 'r') as g:
        for line in g:
            line = line.rstrip()
            length2 = line.split("\t")[1]
            keepLength.append(length2)
    with open(IDbins + "_removed_contig_length_values.txt", 'a') as f:
        for each in removedLength:
            f.write(f'{each}\n')
    with open(IDbins + "_keep_contig_length_values.txt", 'a') as f:
        for each in keepLength:
            f.write(f'{each}\n')
            
    