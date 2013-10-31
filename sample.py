# encoding: utf-8

def sample_map():
	''' Trabalhando com Map '''
	return list(map(lambda x: x**2, range(1,100)))


if __name__ == '__main__':
	print(sample_map())