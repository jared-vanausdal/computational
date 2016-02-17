'''
#################################
##                             ##
##       CH1EX1_PLOT.PY        ##
##                             ##
#################################

This file plots the results obtained from the C++ solutions to Chapter 1
Exercise 1 that were stored in the corresponding .CSV files. 


'''

from multiprocessing import Pool as ThreadPool
import matplotlib.pyplot as plt
import csv
import os
import pylab
import math
import numpy as np

def get_actual(t):
	return math.exp((-4.0)*t)

def plot_data(filename):
	try:
		f = open(str(os.curdir+os.sep+filename))
		f_dict = csv.DictReader(f)
	except:
		print("Error: No such file exists in directory")
		return
	t = []
	u = []
	u_actual = []
	for row in f_dict:
		t.append(row['Time'])
		u.append(row['U'])

	t_actual = np.linspace(0,float(max(t)),100)
	for i in t_actual:
		u_actual.append(get_actual(i))
	plt.plot(t,u,label='Numerical')
	plt.plot(t_actual,u_actual,label='Actual')
	plt.xlabel("Time")
	plt.ylabel("U")
	plt.legend()
	plt.savefig(filename+'.png')
	plt.close()
	
	

def main():
	fileList = ['ExpEuler_n6.csv','ExpEuler_n24.csv','RK4.csv']
	pool = ThreadPool(4)
	pool.map(plot_data,fileList)
	pool.close()
	pool.join()


if __name__ == "__main__":
	main()
