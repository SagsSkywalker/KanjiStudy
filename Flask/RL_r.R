.libPaths(c('C:/Users/Ezequiel/Documents/R/win-library/3.5',
            'C:/Program Files/R/R-3.5.1/library'))
library(caTools)
library(pROC)
library(rjson)
kanji <- read.csv('C:/Users/Ezequiel/Desktop/Flask/kanji.csv')
kanjin <- data.frame(kanji[,5:7])
kanjin$type <- as.numeric(as.factor(kanjin$type))

set.seed(25)
sp <- sample.split(kanjin, SplitRatio = 0.7)

train <- subset(kanjin, sp == 'TRUE')
test <- subset(kanjin, sp == 'FALSE')

a <- roc(train$learnt~train$strokes)
b <- roc(train$learnt~train$type)
ci.auc(a)
ci.auc(b)

m1 <- glm(learnt ~ strokes, train, family = 'binomial')
summary(m1)
dev.res <- c(min(summary(m1)$deviance.resid),
             median(summary(m1)$deviance.resid),
             max(summary(m1)$deviance.resid))
dev.res <- data.frame(dev.res)

coefficients <- summary(m1)$coefficients
coefficients <- data.frame(coefficients)

pred <- predict(m1, test, type = 'response')
plot(round(pred), type = 'l')
t <- table(test$learnt, round(pred))
t <- data.frame(cbind(t[,1:2]))
colnames(t) <- c('c1','c2')
fail <- (1-sum(test$learnt == round(pred))/length(test$learnt))*100
fail <- data.frame(fail)
write(toJSON(c(fail,t, data.frame(round(pred)),dev.res, coefficients)), 'mvdata.json')

