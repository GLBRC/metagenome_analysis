# Metagenome Analysis

This repository houses scripts used in a pipeline to analyze and run QC on metagenome samples.

## Calculate GC content and tetranucleotide frequency with `run.GC.sh`
The `run.GC.sh` script will call two other scripts (`calc.kmerfreq.pl` and `gc.py`) to calculate GC content and tetranucleotide frequency. The script requires a list of files and to indicate the input and output directory:

`bash run.GC.sh ./[output directory] ./[input directory] ./[list of fasta files]`
