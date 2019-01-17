#!/usr/bin/env python

#Source: http://econpy.blogspot.com.au/2011/11/retrieve-stock-price-data-from-yahoo.html

from pandas.io.data import DataReader
from datetime import datetime

#DataReader is what we'll use to retrieve YahooFinance stock price data.
#The DataReader class can also retrieve economic data from two other remote sources
# St.Louis Federal Reserve's FRED database and Kenneth French's Data Library

msft = DataReader("FB", "yahoo", datetime(2014, 5,5))
print msft["Volume"]
print msft["Adj Close"][-100:]
