#Import Library
#Import other necessary libraries like pandas, numpy...
from sklearn import linear_model
 
#Load Train and Test datasets
#Identify feature and response variable(s) and values must be numeric and numpy arrays
x_train=[[2],[3],[5],[8],[9]] # The reason why x should be 2D array is in https://segmentfault.com/q/1010000010743191
y_train=[4,6,10,16,18]
x_test=[[1],[2],[19],[5],[3]]
 
# Create linear regression object
linear = linear_model.LinearRegression()
 
# Train the model using the training sets and check score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)
 
#Equation coefficient and Intercept
print('Coefficient: n', linear.coef_)
print('Intercept: n', linear.intercept_)
 
#Predict Output
predicted= linear.predict(x_test)
print( predicted)

# The output:
#('Coefficient: n', array([2.]))
#('Intercept: n', -1.7763568394002505e-15)
#[ 2.  4. 38. 10.  6.]
