'''
	This python script gets data from both the S&P 500 (^GSPC) Index, and the FTSE 100 (^FTSE) Index from January 3, 1984 to the present.
	The motivation is to look at the volatility, volume, and total dollar amounts of the indices over this time period, comparing the 
	two indices and see what, if any, effect the introduction of a financial transaction tax had on the parameters, listed above, of the 
	FTSE, vs. the S&P500, which is not subject to a transaction tax.
	
'''

from pandas_datareader import data as web
import csv
import os
import datetime


start = datetime.datetime(1984,1,3)
end = datetime.datetime.now()

GSPC = web.DataReader("^GSPC","yahoo",start,end)
FTSE = web.DataReader("^FTSE","yahoo",start,end)

print(GSPC.keys())

