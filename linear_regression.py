import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def linear_regression(file_name):

    #import data
    data = pd.read_csv("data/"+file_name)
    i=0
    column = []
    for col in data.columns:
        column.append(str(i)+'# '+col)
        i=i+1
    print(column)
    X = data.iloc[:,int(input([column , "select parameters X by column index :"]))]
    y = data.iloc[:,int(input([column , "select parameters y by column index :"]))]


    #linear regression
    xy = X*y
    x2 = X**2
    b = (xy.sum()-X.sum()*y.sum()/len(X)) / (x2.sum()-X.sum()**2/len(X))
    a = y.sum()/len(X)-b*X.sum()/len(X)
    y_p = a + b*X
    print('Fitted regression: y = '+str(a)+' + '+str(b)+'x')

    #plot the graph
    data.plot(kind='hexbin',
                x=X.name,
                y=y.name,
                gridsize=20, figsize=(12,8),
                cmap="Blues", sharex=False)

    plt.plot(X, y_p, color='orange')
