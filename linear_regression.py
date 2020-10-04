import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.regression.linear_model as lm
import seaborn as sns

def linear_regression(X, y):
    #linear regression
    xy = X*y
    x2 = X**2
    b = (xy.sum()-X.sum()*y.sum()/len(X)) / (x2.sum()-X.sum()**2/len(X))
    a = y.sum()/len(X)-b*X.sum()/len(X)
    y_p = a + b*X
    print('Fitted regression: y = '+str(a)+' + '+str(b)+'x')
    return y_p
