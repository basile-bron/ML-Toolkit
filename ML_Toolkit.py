import numpy as np
import os
from linear_regression import *
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def choose_file():
    # return list of csv file
    data_files = os.listdir("data/")
    number = int(input([data_files, 'select a file : ']))
    print(data_files[number]+" is selected")
    file_name = data_files[number]
    #import data
    data = pd.read_csv("data/"+file_name)
    return data

def columns_selection(data):
    i=0
    column = []
    for col in data.columns:
        column.append(str(i)+'# '+col)
        i=i+1
    X = data.iloc[:,int(input([column , "select parameters X by column index :"]))]
    y = data.iloc[:,int(input([column , "select parameters y by column index :"]))]
    return X, y

def choose_function(data):
    choice = int(input("choose a function #0 Linear regression, #1 bruteforce :"))
    if choice == 0:
        print("linear regression choosed.")
        X, y = columns_selection(data)
        y_p = linear_regression(X, y)
        plot_graph(data, X, y, y_p)
    elif choice == 1:
        print("bruteforce choosed.")
        brute_force(data)
    else:
        choose_function(data)

def heatmap(data):
    #correlation heatmap
    correlations = data.corr()
    sns.heatmap(correlations)
    """for correlation in correlations.columns:
        X = correlations[correlation]
        if type(X[1]) != type(str()):
            for correlation_bis in correlations.columns:
                y = correlations[correlation_bis]
                if type(y[1]) != type('str') and (col1 != col2) :
                    print()"""

def plot_graph(data, X, y, y_p):
    data.plot(kind='hexbin',
                x=X.name,
                y=y.name,
                gridsize=20, figsize=(12,8),
                cmap="Blues", sharex=False)

    plt.plot(X, y_p, color='orange')
    plt.show()

def brute_force(data):
    for col1 in data.columns:
        X = data[col1]
        if type(X[1]) != type(str()): # this is dirty but i don't have internet (pls don't judge ^^ )
            for col2 in data.columns:
                y = data[col2]
                if type(y[1]) != type('str') and (col1 != col2) :
                    y_p = linear_regression(X, y)
                    plot_graph(data, X, y, y_p)

def main():
    data = choose_file()
    heatmap(data)
    choose_function(data)

if __name__ == '__main__':
    main()
