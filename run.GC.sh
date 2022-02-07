#!/bin/bash

export PATH=/opt/bifxapps/bin:$PATH
export PYTHONPATH=/opt/bifxapps/python/lib/python3.4/site-packages/
export PATH=/opt/bifxapps/hmmer/bin:$PATH
export PATH=/opt/bifxapps/pplacer:$PATH
export PATH=/opt/bifxapps/prodigal:$PATH
export PATH=/opt/bifxapps/bedtools2_2.27.0:$PATH
export PATH=/opt/bifxapps/bbmap:$PATH
export PATH=/opt/bifxapps/prodege-2.2:$PATH
export PATH=/opt/bifxapps/ncbi-blast-2.2.29+:$PATH
export BLASTN_EXE=/opt/bifxapps/ncbi-blast-2.2.29+/bin/blastn
export R_EXE=/usr/bin/R
export PRODIGAL_EXE=/opt/bifxapps/prodigal-2.6.2/prodigal
export PATH=/home/GLBRCORG/pcamejo/biopython-1.66:$PATH

scripts=$HOME/scripts
out=$1
in=$2
ListOfId=$3

#read input file with file names, then run the two scripts
while read y; do
	######
	#runs Michael Noguera's GC.py program to produce tab file with GC content, from fasta file

	python /home/glbrc.org/kmyers/scripts/GC_TF/gc.py $in/$y > $out/$y.GC.tab

	######
	#runs Mad Albertsen script to calculate tetranucleotide frequency per contig
	perl /home/glbrc.org/kmyers/scripts/GC_TF/calc.kmerfreq.pl -i $in/$y -o $out/$y.TF.tab
done < $3
