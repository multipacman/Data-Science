#!/usr/bin/env python
# coding: utf-8

# In[392]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[393]:


dataset = pd.read_csv('updatedAverageTemperatures.csv')
dataset.isnull().any()
dataset = dataset.fillna(method='ffill')

X = dataset.iloc[:, -1].values
y = dataset.iloc[:, 1].values


# In[394]:


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
X_train = X_train.reshape(-1, 1)


# In[395]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[396]:


y_pred = regressor.predict(X_test.reshape(-1, 1))
y_pred


# In[397]:


plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Global Land Average Temperature (Training set)')
plt.xlabel('Years')
plt.ylabel('Land Avg Temp')
plt.show()


# In[398]:


plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Global Land Average Temperature (Test set)')
plt.xlabel('Years')
plt.ylabel('Land Avg Temp')
plt.show()


# In[399]:


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X.reshape(-1, 1), y)


# In[400]:


from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X.reshape(-1, 1))
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# In[401]:


plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X.reshape(-1, 1)), color = 'blue')
plt.title('Globabl Land Average Temperature (Linear Regression)')
plt.xlabel('Years')
plt.ylabel('Land Avg Temp')
plt.show()


# In[402]:


plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X.reshape(-1, 1))), color = 'blue')
plt.title('Global Land Average Temperature (Polynomial Regression)')
plt.xlabel('Years')
plt.ylabel('Land Avg Temp')
plt.show()


# In[403]:


lin_reg.predict([[2016]])


# In[404]:


lin_reg_2.predict(poly_reg.fit_transform([[2016]]))


# In[407]:


predictedValue = {}
for i in range(1,30):
    years = (2016 + i)
    prediction = (lin_reg_2.predict(poly_reg.fit_transform([[years]])))
    predictedValue[years] = np.array2string(prediction)

print('Global Land Average Temperature for the next 30 years (Predicted Values)')
predictedValue

