X=[[2],[3],[5],[8],[9]] # The reason why x should be 2D array is in https://segmentfault.com/q/1010000010743191
y=[1,1,0,0,0]
x_test=[[1],[2],[19],[5],[3]]
#Import Library
from sklearn.linear_model import LogisticRegression
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create logistic regression object
model = LogisticRegression()
 
# Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)
 
#Equation coefficient and Intercept
print('Coefficient: n', model.coef_)
print('Intercept: n', model.intercept_)
 
#Predict Output
predicted= model.predict(x_test)
print predicted
