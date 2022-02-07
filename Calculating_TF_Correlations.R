library(optparse)
parser <- OptionParser()

option_list <- list(
  make_option(c("-d", "--directory"), help = "Directory containing text files", type = "character", action = 'store', dest = "dir")
)

opt <- parse_args(OptionParser(option_list=option_list))

setwd(opt$dir)

TF_files <- list.files(path = opt$dir, pattern = "TF.tab")

for(i in TF_files){
  bin_name <- strsplit(i, split='.fasta')[[1]][1]
  sample <- read.table(file = i, header = TRUE, sep = "\t", row.names = 1)
  sample2 <- t(sample)
  cr <- cor(sample2)
  cr[upper.tri(cr, diag=TRUE)] <- NA
  output <- reshape2::melt(cr, na.rm=TRUE, value.names="cor")
  lowerq = quantile(output$value)[2]
  upperq = quantile(output$value)[4]
  stdev = sd(output$value)
  meanvalue = mean(output$value)
  iqr = upperq - lowerq
  extreme.threshold.lower = lowerq - (iqr * 3)
  mild.threshold.lower = lowerq - (iqr * 1.5)
  stdev.threshold.mild = meanvalue - (stdev)
  stdev.threshold.extreme = meanvalue - (stdev * 2)
  output2 <- output[which((output$value <= extreme.threshold.lower) & (output$value > 0)),]
  output3 <- output[which((output$value <= lowerq) & (output$value > 0)),]
  output4 <- output[which((output$value <= 0.5) & (output$value > 0)),]
  output5 <- output[which((output$value <= stdev.threshold.mild) & (output$value > 0)),]
  output6 <- output[which((output$value <= stdev.threshold.extreme) & (output$value > 0)),]
  fileName = paste(bin_name,"all_correlation_values.txt", sep = "_")
  fileName2 = paste(bin_name,"correlation_values_below_extreme_threshold.txt", sep = "_")
  fileName3 = paste(bin_name,"correlation_values_below_mild_threshold.txt", sep = "_")
  fileName4 = paste(bin_name,"correlation_values_below_0.5.txt", sep = "_")
  fileName5 = paste(bin_name,"correlation_values_below_StDev.txt", sep = "_")
  fileName6 = paste(bin_name,"correlation_values_below_2xStDev.txt", sep = "_")
  write.table(output, file = fileName, col.names = NA, quote = FALSE, sep = "\t")
  write.table(output2, file = fileName2, col.names = NA, quote = FALSE, sep = "\t")
  write.table(output3, file = fileName3, col.names = NA, quote = FALSE, sep = "\t")
  write.table(output4, file = fileName4, col.names = NA, quote = FALSE, sep = "\t")
  write.table(output5, file = fileName5, col.names = NA, quote = FALSE, sep = "\t")
  write.table(output6, file = fileName6, col.names = NA, quote = FALSE, sep = "\t")
}
