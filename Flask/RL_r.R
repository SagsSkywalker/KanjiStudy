.libPaths(c('./3.5'))
#library(caTools)
#library(pROC)
library(rjson)
myArgs <- commandArgs(trailingOnly = TRUE)
myArgs <- as.numeric(myArgs)
kanji <- read.csv('kanji.csv')
kanji$learnt[myArgs[1]] <- myArgs[2]
write.csv(kanji, file = 'kanji.csv', row.names = FALSE)
kanjin <- data.frame(kanji[,5:7])
kanjin$type <- as.numeric(as.factor(kanjin$type))

set.seed(25)
#sp <- sample.split(kanjin, SplitRatio = 0.7)

#train <- subset(kanjin, sp == 'TRUE')
#test <- subset(kanjin, sp == 'FALSE')

#a <- roc(train$learnt~train$strokes)
#b <- roc(train$learnt~train$type)
#ci.auc(a)
#ci.auc(b)

#m1 <- glm(learnt ~ strokes, train, family = 'binomial')
m2 <- glm(learnt ~ strokes, kanji, family = 'binomial')
#summary(m1)
summary(m2)
#dev.res <- c(min(summary(m1)$deviance.resid),
#             median(summary(m1)$deviance.resid),
#             max(summary(m1)$deviance.resid))
#dev.res <- data.frame(dev.res)

#coefficients <- summary(m1)$coefficients
#coefficients <- data.frame(coefficients)

#pred <- predict(m1, test, type = 'response')
pred1 <- predict(m2, kanji, type = 'response')
plot(round(pred1), type = 'l')
#t <- table(test$learnt, round(pred))
#t <- data.frame(cbind(t[,1:2]))
#colnames(t) <- c('c1','c2')
#fail <- (1-sum(test$learnt == round(pred))/length(test$learnt))*100
#fail <- data.frame(fail)
fail <- (1-sum(kanji$learnt == round(pred1))/length(kanji$learnt))*100
fail
#write(toJSON(c(fail,t, data.frame(round(pred)),dev.res, coefficients)), 'mvdata.json')
kanji <- cbind(kanji, clasification = c(round(pred1)))
write(toJSON(c(kanji)), 'mvdata.json')
