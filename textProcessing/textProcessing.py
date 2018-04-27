'''
--------------------------------------
	Created by Qiwei Bao on 12/15/2017
--------------------------------------
'''
import re
import os 
import logging
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

from scipy.signal import fir_filter_design as ffd
from scipy.signal import filter_design as ifd

'''
read pedometer data and 
'''

# Read names of all the files from a direcotry
def readDataFromFile(dir):
    pedometerData = open(dir)
    pedometerData = [i[63:] for i in  pedometerData]
    return pedometerData

def selectOutput(data):
	res = [0]
	ad = 0
	for i in data:
		if ("Output" in i) and (float(i[8:15]) < 4.5):
			# res.append(float(i[8:15]) + res[-1])
			res.append(float(i[8:15]))
			# print res[-1]
	return res[1:]

# select distance from steps
def selectDistance(data):
	res = [0]
	ad = 0
	for i in data:
		if ("Distance for this step" in i) and (float(i[27:35]) < 30):
			# res.append(float(i[8:15]) + res[-1])
			res.append(float(i[27:35]))
			# print res[-1]
	return res[1:]

# select step from steps
def selectStep(dir, data):
	res = []
	pedometerData = open(dir)
	pedometerData = [i for i in  pedometerData]
	i = 0
	while (i < len(data)):
		if ("This is the" in data[i]):
			res.append(pedometerData[i][6:18])
		i += 1
	return res

def sumDistance(data):
	res = [0]
	for d in data:
		d += res[-1]
		res.append(d)
	return res[1:]

def calDistance(time, data):
	dis = [0]
	i = 0
	for i in range(len(time)):
		dis.append(data[i] * time[i] * time[i] / 1000000 + dis[-1])
	return dis[1:]

def calAcc(time, data):
	acc = [0]
	i = 0
	for i in range(len(time)):
		acc.append(data[i] / (time[i] * time[i] / 1000000))
	return acc[1:]

def selectTime(dir, data):
	res = []
	pedometerData = open(dir)
	pedometerData = [i for i in  pedometerData]
	i = 0
	while (i < len(data)):
		if ("Output" in data[i]) and (float(data[i][8:15]) < 4.5):
			res.append(pedometerData[i][6:18])
		i += 1
	return res

def timeFormat(time):
	res = []
	res_t = 0
	# 04:00:14.165
	for t in time:
		#print t[:2], t[3:5], t[6:]
		res_t = int(t[:2]) * 3600 + int(t[3:5]) * 60 + float(t[6:]) + 2000
		res.append(res_t)
	return res

def lpf(s):
	fc = 0.1  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
	b = 0.08  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
	N = int(np.ceil((4 / b)))
	if not N % 2: N += 1  # Make sure that N is odd.
	n = np.arange(N)
	 
	# Compute sinc filter.
	h = np.sinc(2 * fc * (n - (N - 1) / 2.))
	 
	# Compute Blackman window.
	w = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + \
	    0.08 * np.cos(4 * np.pi * n / (N - 1))
	 
	# Multiply sinc filter with window.
	h = h * w
	 
	# Normalize to get unity gain.
	h = h / np.sum(h)
	s = np.convolve(s, h)
	return s

def drawChart(time, data, step_time):
	plt.figure()
	x = []
	step_time_x = []
	for j in range(len(step_time)):
		step_time_x.append(j * 6100)
	diff = []
	for i in range(len(step_time)):
		for j in range(len(time)):
			if step_time[i] == time[j]:
				diff.append(data[j] - step_time_x[i])
				# print data[j]
	for i in diff:
		print i / 500


	#print data[0]
	#plt.plot(time, data, x, avg)
	plt.plot(time, data, step_time, step_time_x)
	# plt.show()
	
	plt.savefig("acc_compare_distance.png")  




dir = "/Users/qiweibao/Data/IndoorData/pedometer_Dec_15.txt"
data = readDataFromFile(dir)
output = selectOutput(data)
res = []
for i in output:
	i = i / 25
	res.append(i)
output = res
time = selectTime(dir, data)
time = timeFormat(time)
step_time = selectStep(dir, data)
step_time = timeFormat(step_time)

sum = 0
res = []
for i in output:
	i = i * 100
	res.append(i)
	sum += i 
output = res
avg_output = sum / len(output)
# print avg_output
output = calDistance(time, output)

#print out each step
'''tmp = output[0]
for i in range(len(output)):
	print output[i] - tmp
	tmp = output[i]'''

drawChart(time, output, step_time)
# output = calAcc(time, output)
# output = lpf(output)
# print len(time), len(output)
# drawChart(time, output)
'''output = calAcc(time, output)
drawChart(time, output)'''