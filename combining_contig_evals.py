#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to combine data and identify results to delete for Metadata analysis.
Uses results from ProDeGe (contam results), contig lengths, correlation R script
to identify potential contigs that should be removed from each Bin.
Created on Wed Feb 26 11:21:22 2020

@author: kevinmyers
"""
import os

cwd = os.getcwd()

all_files = []

all_files = [ fn for fn in os.listdir(os.getcwd()) if fn.endswith("contig_lengths.txt") ]

bins = []
for each in all_files:
    binID = each.split("_contig")[0]
    if binID in bins:
        pass
    else:
        bins.append(binID)
        
for IDbins in bins:
    contigs = {}
    with open(IDbins + '_remove_updated_headers.txt') as f:
        for line in f:
            contig = line.split('\n')[0]
            if contig in contigs:
                pass
            else:
                contigs[contig] = []
    
    with open(IDbins + '_contig_lengths.txt') as f:
        for line in f:
            name = line.split('\t')[0]
            length = line.split('\t')[1]
            if name in contigs:
                contigs[name] = length
    
    corr = {}
    with open(IDbins + '_correlation_values_below_2xStDev.txt') as f:
        next(f)
        for line in f:
            name1 = line.split('\t')[1]
            name2 = line.split('\t')[2]
            if name1 in corr:
                pass
            else:
                corr[name1] = []
            if name2 in corr:
                pass
            else:
                corr[name2] = []
    
    final = []
    for k in contigs:
        if k in corr:
            final.append(f"{k}\t{contigs[k]}")
    
    with open(IDbins + '_contigs_to_remove.txt', 'w') as f:
        f.write(f"#Contigs that were flagged for removal by ProDeGe and show a low tetranucleotide frequency compared to other contigs in the same bin. Also shown is the contig length.\n\n")
        f.write(f"Congig\tLength (bp)\n")
        for each in final:
            f.write(each)