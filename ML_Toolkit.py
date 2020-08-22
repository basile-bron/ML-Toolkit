import os
from linear_regression import *
def choose_file():
    data_files = os.listdir("data/") # return list
    print(data_files)
    number = int(input([data_files, 'select a file : ']))
    print(data_files[number]+" is selected")
    file_name = data_files[number]
    return file_name

def main():
    file_name = str(choose_file())
    linear_regression(file_name)

if __name__ == '__main__':
    main()
