
import csv



# Candle

def create(date, open, high, low, close, volume):
	return Candle(date, open, high, low, close, volume)



class Candle:

	def __init__(self, date, open_, high, low, close, volume):
		self._date = date
		self._open = open_
		self._high = high
		self._low = low
		self._close = close
		self._volume = volume


	def date(self):
		return self._date


	def open(self):
		return self._open


	def high(self):
		return self._high


	def low(self):
		return self._low


	def close(self):
		return self._close


	def volume(self):
		return self._volume


	def is_bullish(self):
		return self._low < self._high


	def is_bearish(self):
		return self._low > self._high


	def is_unit(self):
		return self._low == self._high


	def current(self):
		if self.is_bullish():
			return self._high
		elif self.is_bearish():
			return self._low
		else:
			return self._high


	def __eq__(self, other):
		return self._date == other.date() and self._open == other.open() and self._high == other.high() and \
				self._low == other.low() and self._close == other.close() and self._volume == other.volume() and \
				self._volume == other.volume()


	def __str__(self):
		return "Japan candle, data: %s, open: %s, high: %s, low: %s, close: %s, volume: %s" % \
				(self._date, self._open, self._high, self._low, self._close, self._volume)


							