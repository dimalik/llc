## there are 20 texts in corpus
texts <- 1:20

## empty data.frame
alltexts <- data.frame()

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

    ## build a data.frame of all texts
    alltexts <- rbind(alltexts, newtext)

}


surps <- read.delim('~/Corpora/DundeeCorpus/surprisal.txt', header = F)
