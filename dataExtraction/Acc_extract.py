'''
extract Acc data from text and save to a csv file.
'''

import os
import re
import csv
import matplotlib.pyplot as plt
import numpy as np 

method_list_tmp = []
method_list_fold = []
time = []
acc = []
dis = []

# read data from file
def readfile(dir):
    file = open(dir)
    while True:
        read = file.readline()
        if not read:
            break
        else:
            method = read.split()
            if len(method) == 1:
            	method_list_tmp.append(method[0])
            elif len(method) > 1:
            	time = method[1].split(':')
            	tmp_time = int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])
            	method_list_tmp.append(str(tmp_time))
            	method_list_tmp.append(method[-1])
            '''for data in method:
                if re.search('.*([a-zA-Z]+).*', data):
                	break
                else:
                    method_list_tmp.append(data)
    method_list_tmp.sort()'''
    return method_list_tmp

# Save data to CSV file
def savefile(dir):
    for i in range(len(method_list_tmp) / 4):
        method_list_fold.append(method_list_tmp[4*i] + ',' + method_list_tmp[4*i + 1] + ',' + method_list_tmp[4*i + 2] + ',' + method_list_tmp[4*i + 3])
    output = open(dir, 'wb+')
    for i in method_list_fold:
        output.write(str(i))
        output.write("\n")
    output.close()

def readaccdata(dir):
    file = open(dir)
    while True:
        read = file.readline()
        if not read:
            break
        else:
        	data = read.split()
        	time.append(data[0])
        	acc.append(data[1])
def calc():
    for i,j in time, acc:
        dis.append(i * j * j)
        print dis
    plt.plot(time, dis)
    plt.show() 

            
if __name__ == "__main__":
    dir = "/Users/qiweibao/Data/IndoorData/acc_afterfilter_Apr_25.txt"
    readaccdata(dir)
    calc()
    '''path = "/Users/qiweibao/Desktop/data/straight3.txt"
    pathwrite = "/Users/qiweibao/Desktop/data/straight3_test.txt"
    filenames = readfile(path)
    savefile(pathwrite)'''

