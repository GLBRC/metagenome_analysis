#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove contigs marked as contaminated using combining_contig_evals.py script

Read in the results from the samtools idxstats that lists number of reads that 
align per contig. Remove the contaminated contigs and store the sum of the 
aligned read number for each rep (3rd column). Then for each bin, average the sums from
each replicate.

Requires "contigs_to_remove.txt" file for each Bin
Requires Samtools IDXstats for each replicate (for each Bin)

Created on Wed Mar  4 13:52:35 2020

@author: kevinmyers
"""
import glob
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

combined = []
        
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
    idxstat_files = []
    for name in glob.glob(IDbins+'*sort_output.txt'):
        idxstat_files.append(name)
        
    sums = []
    for each in idxstat_files:
        values = []
        contigs_to_keep = []
        with open(each, 'r') as f:
            for line in f:
                contig = line.split('\t')[0]
                value = line.split('\t')[2]
                if contig not in contigs:
                    values.append(int(value))
                    contigs_to_keep.append(contig)
                else:
                    pass
            sums.append(sum(values))
    averages = []
    if len(sums)>0:
        #averages.append(sum(sums)/float(len(sums)))
        averages.append(sum(sums))
    else:
        averages.append("0")
    with open(IDbins+'_cleaned_contig_sums.txt', 'w') as f:
        f.write('Sum of all aligned read value for all cleaned contigs\n\n')
        for each in averages:
            f.write(f'{each}\n')
            combined.append(f"{IDbins}\t{each}\n")
        f.write('\nSums of aligned reads for each cleaned contigs\n\n') 
        for each in sums:
            f.write(f'{each}\n')
        f.write('\n\nContigs we keep and calculate the values of as above\n\n')
        for each in contigs_to_keep:
            f.write(f'{each}\n')

with open("Summary_of_All_Aligned_Reads_Summed_Over_Reps.txt", "a") as f:
    f.write("Bin\tAligned_Reads\n")
    for each in combined:
        f.write(each)