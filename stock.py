
try:
	from . import candle
except:
	import candle

import csv



# Stock

def load(name):
	assert len(name) > 0

	file = []

	with open('data/' + name + '.txt', newline = '') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			file.append(row)

	candles = []

	for dictionary in file:
		c = candle.create(dictionary["Date"], 
							dictionary["Open"], 
							dictionary["High"], 
							dictionary["Low"], 
							dictionary["Close"], 
							dictionary["Volume"])

		candles.append(candle)


	return create(name, candles)



def create(name, candles):
	return Stock(name, candles)



class Stock:

	def __init__(self, name, candles):
		self._name = name

		self._candles = candles


	def name(self):
		return self._name


	def candles(self):
		return self._candles


	def dates(self):
		return self._dates


	def __eq__(self, other):
		return self._name == other.name() and self._candles == other.candles()


	def __str__(self):
		return "Stock, name: %s, candles: %s" % (self._name, self._candles)



		