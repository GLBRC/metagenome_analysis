# Metagenome Analysis

This repository houses scripts used to analyze and run QC on metagenome samples.

## Calculate GC content and tetranucleotide frequency with `run.GC.sh`
The `run.GC.sh` script will call two other scripts (`calc.kmerfreq.pl` and `gc.py`) to calculate GC content and tetranucleotide frequency. The script requires a list of files and to indicate the input and output directory:

`bash run.GC.sh ./[output directory] ./[input directory] ./[list of fasta files]`

## `make_prodege_config_files.py`
Simple script to make ProDeGe config files given a list of FASTA files

Requires file with fasta files names on every line
Requires directory where fasta files are located

Must be run in the directory were to save the results

## `Calculating_TF_Correlations.R`
Rscript to calculate the correlations from the `run.GC.sh` results and produce a number of files

## `combining_contig_evals.py`
Script to combine data and identify results to delete for Metadata analysis.
Uses results from ProDeGe (contam results), contig lengths, correlation R script
to identify potential contigs that should be removed from each Bin.

## `remove_contam_contigs.py`
Remove contigs marked as contaminated using `combining_contig_evals.py` script

Read in FASTA and corresponding contigs_to_remove.txt file, match, keep only contigs
not present in the contigs_to_remove.txt file

## `remove_contigs_sum_read_count.py`
Remove contigs marked as contaminated using `combining_contig_evals.py` script

Read in the results from the samtools idxstats that lists number of reads that 
align per contig. Remove the contaminated contigs and store the sum of the 
aligned read number for each rep (3rd column). Then for each bin, average the sums from
each replicate.

Requires "contigs_to_remove.txt" file for each Bin
Requires Samtools IDXstats for each replicate (for each Bin)

## `contig_length_organization.py`
Script to organize the contig lengths for passed (cleaned) and removed (contaminated)
contigs into two files. Each line in the file is a contig length.

## `make_histogram_boxplot_contig_lengths.R`
Rscript to make histograms and boxplots from the contig length files.

## `autoML.py`

Scripts for machine learning, specifically on classifying MAGs from different agroindustrial residues using known lactic acid, chain elongators, and lachnospiraceae genomes. Results are from metabolism identification script for both training and testing files.

Using [this site](https://www.freecodecamp.org/news/classification-with-python-automl/) as a guide.

Requires pandas, numpy, and AutoML python modules

## `NMDS_R_commands_20220118.R`

Script used to construct NMDS plots. All required files are located in the Example Files.

Requires ggplot2, dplyr, cowplot, ggthemes, RColorBrewer, tidyverse, forcats, and vegan R libraries
