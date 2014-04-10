#THIS CODE SPLITS THE DATES AND THE HOURS
#JUST CHANGE THE CSV IT'S READING IN TO BE THE RIGHT FILE
data <- read.csv('/home/kirk/revised.csv', stringsAsFactors=FALSE,header=TRUE)
g <- substr(data$IntervalStart, -5, 10)
data$date <- sapply(strsplit(g, " "), "[[", 1)
data$hour <- rep(seq(from=0, to=23, by=1),length.out=length(data$IntervalStart)) 
#WRITE THIS OUT WITH THE BUILDING NAME
#THEN READ THIS FILE INTO PYTHON
write.csv(data, "revised.csv")

