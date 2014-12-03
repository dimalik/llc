## there are 20 texts in corpus
texts <- 1:20

## empty data.frame plus counter
alltexts <- data.frame()
priorcum <- 0

## for each text
for (n in texts) {
    ## make the filepath
    if (n < 10) {
       filepath <- paste("~/Corpora/DundeeCorpus/tx0", n, "wrdp.dat", sep="")
    }
    else {
       filepath <- paste("~/Corpora/DundeeCorpus/tx", n, "wrdp.dat", sep="")
    }

    ## read in file
    newtext <- read.delim(filepath, header = F, sep = "")
    priorcount <- nrow(newtext)
    priorcum <- priorcum + priorcount

    ## grab the relevant columns, give headers, calculate the cumulative line number
    relevant <- data.frame(newtext[, 1:5], newtext[, 13])
    colnames(relevant) <- c("WORD", "TEXT", "SCREEN", "LINE", "POSITION", "WNUM")
    relevant$LINENUMCUM <- ((relevant$SCREEN - 1 ) * 5) + relevant$LINE

    ## for each line
    lines <- unique(relevant$LINENUMCUM)
    for (line in lines) {
    	## subset only the words occurring on this line
    	thisline <- subset(relevant, LINENUMCUM == line)

	## how many words (rows) on this line?
	maxline <- nrow(thisline)

	## if more than 1, need to remove the final word
	if (maxline > 1) {
	    lastwnum <- thisline$WNUM[maxline]
	    relevant <- relevant[-lastwnum,]
	}

	## remove the first word
	firstwnum <- thisline$WNUM[1]
    	relevant <- relevant[-firstwnum,]
    }
    ## new size of df
    newcount <- nrow(relevant)

    ## build a data.frame of all texts
    alltexts <- rbind(alltexts, relevant)

    ## print infolines
    print(paste("Processed text", n))
    print(paste("Reduced from", priorcount, "lines to", newcount, "lines"))
}

## overall infoline
newtotal <- nrow(alltexts)
print("END")
print(paste("Total reduction:", priorcum, "lines to", newtotal, "lines"))

## print to file
#str(alltexts)
write.table(alltexts, "~/Corpora/DundeeCorpus/textReduction1.txt", sep="\t", quote = FALSE, row.names = FALSE)
