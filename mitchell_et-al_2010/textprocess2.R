
reduced <- read.delim("~/Corpora/DundeeCorpus/textReduction1.txt")
reduced$WID <- paste(reduced$TEXT, reduced$WNUM, sep="")

subjs <- c('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
texts <- 1:20
wdCount <- 0

accumulate <- data.frame()
for (subj in subjs) {

    for (text in texts) {
        if (text < 10) {
	   filein <- paste("~/Corpora/DundeeCorpus/s", subj, "0", text, "ma1p.dat", sep="")
	}
	else {
    	   filein <- paste("~/Corpora/DundeeCorpus/s", subj, text, "ma1p.dat", sep="")
	}

	print(filein)
	eyetrack <- read.csv(filein, sep="", quote="", skipNul = TRUE)
	colnames(eyetrack)[2] <- "SCREEN"
	eyetrack$TEXT <- text
	eyetrack$WID <- paste(eyetrack$TEXT, eyetrack$WNUM, sep="")

	wnumcheck <- 0
	screens <- unique(eyetrack$SCREEN)

	for (screen in screens) {
	    print(paste("subject:", subj, "text:", text, "screen:", screen))
	    scr <- subset(eyetrack, SCREEN == screen)
	    lines <- unique(scr$LINE)

	    linecheck <- 0
	    for (line in lines) {
	        if (line > 0) {
		        if (line == linecheck+1) {
			   print(paste("line", line, "fine"))
			   ln <- subset(scr, LINE == line)
			   wnums <- unique(ln$WNUM)

			   for (wnum in wnums) {
			       if (wnum > 0) {
			       	  if (wnum == wnumcheck+1) {
				     print(paste("wnum", wnum, "fine"))
				     wdCount <- wdCount + 1
				     wd <- subset(ln, WNUM == wnum)
				     if (length(which(ln$LAUN > 0)) < 1) {
				       print(paste(wd$WORD[1], "accepted"))
				       wdadd <- wd[1,]
				       wdadd$FDUR[1] <- sum(wd$FDUR)
				       wdadd$LAUN[1] <- sum(wd$LAUN)
				       accumulate <- rbind(accumulate, wdadd)
				     }
				     else {
				       print(paste(wd$WORD[1], "rejected due to R->L saccade(s)"))
				     }
				  }
				  else {
				       print(paste("wnum", wnum, "not fine"))
				  }
				  wnumcheck <- wnum
	     		       }
	   		   }
			}
			else {
			     print(paste("line", line, "not fine"))
			}
			linecheck <- line
		}
	   }
       }
    }
}
print(paste(wdCount, "possible words"))
write.table(accumulate, "~/Corpora/DundeeCorpus/textReduction2.txt", sep="\t", quote = FALSE, row.names = FALS)E

## final reduction
priorcount <- nrow(accumulate)
## punctuation
accumulate <- accumulate[-(which(accumulate$OLEN > accumulate$WLEN)), ]
newcount1 <- nrow(accumulate)
write.table(accumulate, "~/Corpora/DundeeCorpus/textReduction3.txt", sep="\t", quote = FALSE, row.names = FALSE)
## reduction
accumulate <- accumulate[accumulate$WID %in% reduced$WID,]
newcount2 <- nrow(accumulate)
write.table(accumulate, "~/Corpora/DundeeCorpus/textReduction4.txt", sep="\t", quote = FALSE, row.names = FALSE)
## stopwords
library(tm)
stpwds <- stopwords("en")
accumulate <- accumulate[tolower(accumulate$WORD) %in% stpwds,]
write.table(accumulate, "~/Corpora/DundeeCorpus/textReduction5.txt", sep="\t", quote = FALSE, row.names = FALSE)
newcount3 <- nrow(accumulate)

## infoline
print(paste("reduced from", priorcount, "lines to", newcount1, "lines after removal of punctuated words, to", newcount2, "lines after removal of first/last words, to", newcount3, "lines after removal of stopwords"))
