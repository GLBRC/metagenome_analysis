#Make heatmap for contig length

#packages = c("optparse")

#package.check <- lapply(
#  packages,
#  FUN = function(x) {
#    if (!require(x, character.only = TRUE)) {
#      install.packages(x, dependencies = TRUE)
#      library(x, character.only = TRUE)
#    }
#  }
#)

library(optparse)
parser <- OptionParser()

option_list <- list(
  make_option(c("-d", "--directory"), help = "Directory containing text files", type = "character", action = 'store', dest = "dir"),
  make_option(c("-o", "--output_prefix"), help = "Signify prefix for output files", action = "store", type = "character", default = "output_", dest = 'output')
)

opt <- parse_args(OptionParser(option_list=option_list))

setwd(opt$dir)

histogram_out = paste(opt$output, "histogram_passed_failed_contig_lengths.png", sep = "_")
boxplot_out = paste(opt$output, "boxplot_passed_failed_contig_lengths.png", sep = "_")

keep <- read.table(file = "combined_keep_contig_length_values.txt", header = FALSE)
remove <- read.table(file = "combined_removed_contig_length_values.txt", header = FALSE)

png(filename=histogram_out, res = 300, width = 8, height = 11, units = 'in')
hist(keep$V1, breaks = 10000, col=rgb(1,0,0,0.5), xlim = c(0,50000), xlab = "Contig length (bp)", main = "Comparing Passed (red) and Failed (blue) Contig Lengths", freq=TRUE, ylim = c(0,1000))
hist(remove$V1, breaks = 100, col=rgb(0,0,1,0.5), add=TRUE, freq=T)

png(filename=boxplot_out, res = 300, width = 8, height = 11, units = 'in')
boxplot(keep$V1, remove$V1, ylim=c(0,50000), col=c(rgb(1,0,0,0.5),rgb(0,0,1,0.5)), main = "Comparing Passed (red) and Failed (blue) Contig Lengths", xlab = "Contig Category", ylab = "Contig Length (bp)", names = c("Passed", "Failed"))
