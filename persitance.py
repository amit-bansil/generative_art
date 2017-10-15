from operator import mul
from math import floor

def reverse_digits(n, base):
	if base < 2:
		raise Exception('base: %d < 2' % base)
	while n > 0:
		yield n % base
		n = int(floor(n / base))

def digits(n, base):
	return list(reverse_digits(n, base))[::-1]

def product_of_digits(n, base):
	return reduce(mul, digits(n, base), 1)

def persist(n, base):
	while n >= base:
		yield n
		n = product_of_digits(n, base)
	yield n

def list_persist(n, base):
	return list(persist(n, base))

def persistance(n, base):
	return len(list_persist(n, base)) - 1

def root(n, base):
	return list_persist(n, base)[-1]

def row(list):
	return '\t'.join(map(str,list))

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def plot(x0, y0, size, resolution):
	base = int(resolution / size)
	x0 = int(x0 * base)
	y0 = int(y0 * base)
	length = int(size * base)

	P = np.zeros((length,length), dtype=np.int)
	for x in range(x0,x0+length):
		print x
		for y in range(y0,y0+length):
			px = int(x-x0)
			py = int(y-y0)
			p = persistance(x + y * base, base)
			P[px][py] = p
	fig = plt.imshow(P,interpolation='nearest')
	fig.set_cmap('hot')
	plt.axis('off')
	plt.show()


plot(0, 0, 1, 2000)

#radius = persistance
#arcs = 3d hops whose height is their length 
#type number/formula to see connections for set
#force directed to work out angles
#color sets to compare
#share