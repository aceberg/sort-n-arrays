#!/usr/bin/python3

import sys
from random import randint

max_size = 10 # MUST BE BIGGER THEN N
arr_size = []

def gen_sizes(n):
	for i in range(0,n):
		k = randint(2, max_size)
		while k in arr_size:
			k = randint(2, max_size)
		arr_size.append(k)


def gen_array(k):
	one_array = []
	for i in range(0,arr_size[k]):
		one_array.append(randint(0, 100))
	return one_array

def main():
	one_array = []
	n_arrays = []
	n = int(sys.argv[1])
	print('n =',n)
	gen_sizes(n)
	print('array sizes:',arr_size)
	
	for i in range(0,n):
		one_array=gen_array(i)
		print(i,':',one_array)
		n_arrays.append(one_array)

	for i in range(0,n):
		if (i % 2 == 0):
			n_arrays[i].sort()
		else:
			n_arrays[i].sort(reverse=True)
		print(i,':',n_arrays[i])
		
	return n_arrays
	
	
if __name__ == "__main__":
    main()
