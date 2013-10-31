# encoding: utf-8
from functools import reduce

def sample_map():
	''' Trabalhando com Map '''
	return list(map(lambda x: x**2, range(1,100)))

def sample_reduce():
	''' Trabalhando com Reduce'''
	return reduce(lambda x, y: x+y, range(1, 100))

if __name__ == '__main__':
	print(sample_reduce())
