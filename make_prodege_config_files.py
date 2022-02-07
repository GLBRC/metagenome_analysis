#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:04:52 2021

Simple script to make ProDeGe config files given a list of FASTA files

Requires file with fasta files names on every line
Requires directory where fasta files are located

Must be run in the directory were to save the results

@author: kevinmyers
"""

import argparse
import os
import sys

def makeConfig( each, FASTAdir ):
    output = each + "_config.cfg"
    fastaFile = each + ".fasta"
    inputDir = FASTAdir + f"{fastaFile}"
    with open(output, 'a') as f:
        f.write(f'TAXON_DISPLAY_NAME="{each}"\n')
        f.write('TAXON_DOMAIN=Bacteria\n')
        f.write('TAXON_PHYLUM=\n')
        f.write('TAXON_CLASS=\n')
        f.write('TAXON_ORDER=\n')
        f.write('TAXON_FAMILY=\n')
        f.write('TAXON_GENUS=\n')
        f.write('TAXON_SPECIES=\n')
        f.write('INSTALL_LOCATION=/opt/bifxapps/prodege\n')
        f.write('WORKING_DIR=./\n')
        f.write(f"IN_FASTA={inputDir}\n")
        f.write(f"JOB_NAME={each}\n")
        f.write("RUN_GENECALL=1\n")
        f.write("RUN_BLAST=1\n")
        f.write("RUN_CLASSIFY=1\n")
        f.write("RUN_ACCURACY=1\n")
        f.write("BLAST_THREADS=32")
    
    cwd   = os.getcwd()
    
    configFiles = [ fn for fn in os.listdir(cwd) if fn.endswith(".cfg") ]
    
    with open("config_files.txt", "w") as out:
        for each in configFiles:
            out.write(f"{each}\n")       
    
    
def main():
    files = []
    
    cmdparser = argparse.ArgumentParser(description="Make ProDeGe config files.",
                                        usage='%(prog)s -f <fasta file list> -d <directory with FASTA files>' ,prog='make_prodege_config_files.py'  )                                  
    cmdparser.add_argument('-f', '--file', action='store', dest='FILE' , help='File with FASTA files to use, one per line.', metavar='')
    cmdparser.add_argument('-d', '--dir', action='store', dest='DIR', help='Directory where FASTA files are located.', metavar='')
    cmdResults = vars(cmdparser.parse_args())
    
    if cmdResults['FILE'] is not None:
        input_file = cmdResults['FILE']
    else:
        print("Please provide an input file listing the FASTA files to use.\n")
        cmdparser.print_help()
        sys.exit(1)
        
    with open(input_file,"r") as f:
        for line in f:
            file = line.split('.')[0]
            files.append(file)
            
    if cmdResults['DIR'] is not None:
        FASTAdir = cmdResults['DIR']
    else:
        print("Please provide the directory where the FASTA are located.\n")
        cmdparser.print_help()
        sys.exit(1)
            
    for each in files:
        makeConfig( each, FASTAdir )
        
if __name__ == "__main__":
    main()