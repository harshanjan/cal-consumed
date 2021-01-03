cal <- read.csv(file.choose())
attach(cal)
View(cal)
#linear regression model
plot(cal$Weight.gained..grams.,cal$Calories.Consumed)
cor(Calories.Consumed,Weight.gained..grams.)
model <- lm(Weight.gained..grams.~Calories.Consumed)
summary(model)

confint(model,level = .95)

pred <- predict(model,interval = "predict")
pred <- as.data.frame(pred)
View(pred)

rmse <- sqrt(mean(model$residuals^2))
rmse


#log
plot(Weight.gained..grams.,log(Calories.Consumed))
cor(Weight.gained..grams.,log(Calories.Consumed))
model1 <- lm(Weight.gained..grams.~log(Calories.Consumed))
summary(model1)

confint(model1,level = .95)

pred1 <- predict(model1,interval = "predict")
pred1 <- as.data.frame(pred1)
View(pred1)

cor(pred$fit,Weight.gained..grams.)
    
rmse1 <- sqrt(mean(model1$residuals^2))
rmse1

#exponential model
plot(log(Weight.gained..grams.),Calories.Consumed)
cor(log(Weight.gained..grams.),Calories.Consumed)
model2 <- lm(log(Weight.gained..grams.)~Calories.Consumed)
summary(model2)

confint(model2,level = .95)

pred2 <- predict(model2,interval = "predict")
pred2 <- as.data.frame(pred2)
View(pred2)
pred2 <- exp(pred2)
pred2
err <- pred2$fit - Weight.gained..grams.
View(err)

cor(pred$fit,log(Weight.gained..grams.))

rmse2 <- sqrt(mean(err^2))
rmse2

#polynomial model

cor(log(Weight.gained..grams.),(Calories.Consumed+I(Calories.Consumed*Calories.Consumed)))
model3 <- lm(log(Weight.gained..grams.)~Calories.Consumed+ I(Calories.Consumed*Calories.Consumed))
summary(model3)

confint(model3,level = .95)

pred3 <- predict(model3,interval = "predict")
pred3 <- as.data.frame(pred3)
View(pred3)
pred3 <- exp(pred3)
pred3
err1 <- Weight.gained..grams.- pred3$fit
View(err1)


cor(pred3$fit,log(Weight.gained..grams.))

rmse3 <- sqrt(mean(err1^2))
rmse3



