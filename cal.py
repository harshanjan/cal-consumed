
import pandas as pd   
import numpy as np 

datas = pd.read_csv("C:/Users/user/desktop/datasets/calories_consumed.csv")
datas=datas.rename(columns={"Weight gained (grams)":"weightgained"})
datas=datas.rename(columns={"Calories Consumed":"caloriesconsumed"})
import matplotlib.pylab as plt 

plt.scatter(x=datas['weightgained'],y=datas['caloriesconsumed'],color='green')
np.corrcoef(x=datas['weightgained'],y=datas['caloriesconsumed'])

#linear transformation

import statsmodels.formula.api as smf
model = smf.ols('caloriesconsumed~weightgained',data=datas).fit()
model.summary()

pred1 = model.predict(pd.DataFrame(datas['weightgained']))
pred1
print (model.conf_int(0.05)) 

res = datas.caloriesconsumed - pred1
sqres = res*res
mse = np.mean(sqres)
rmse = np.sqrt(mse)




# Log Transformation

plt.scatter(x=np.log(datas['weightgained']),y=datas['caloriesconsumed'],color='brown')
np.corrcoef(np.log(datas.weightgained), datas.caloriesconsumed)

model2 = smf.ols('caloriesconsumed ~ np.log(weightgained)',data=datas).fit()
model2.summary()

pred2 = model2.predict(pd.DataFrame(datas['weightgained']))
pred2
print(model2.conf_int(0.05))

res2 = datas.caloriesconsumed - pred2
sqres2 = res2*res2
mse2 = np.mean(sqres2)
rmse2 = np.sqrt(mse2)

# Exponential transformation
plt.scatter(x=datas['weightgained'], y=np.log(datas['caloriesconsumed']),color='orange')

np.corrcoef(datas.weightgained, np.log(datas.caloriesconsumed)) 

model3 = smf.ols('np.log(caloriesconsumed) ~ weightgained',data=datas).fit()
model3.summary()

pred_log = model3.predict(pd.DataFrame(datas['weightgained']))
pred_log
pred3 = np.exp(pred_log)
pred3
print(model3.conf_int(0.05))

res3 = datas.caloriesconsumed - pred3
sqres3 = res3*res3
mse3 = np.mean(sqres3)
rmse3 = np.sqrt(mse3)

#poly

model4 = smf.ols('np.log(caloriesconsumed)~weightgained+I(weightgained*weightgained)',data=datas).fit()
model4.summary()

pred4_log2 = model4.predict(pd.DataFrame(datas['weightgained']))
pred4_log2
pred4 = np.exp(pred4_log2)
pred4
print (model4.conf_int(0.05))
res4 = datas.caloriesconsumed - pred4
sqres4 = res4*res4
mse4 = np.mean(sqres4)
rmse4 = np.sqrt(mse4)
