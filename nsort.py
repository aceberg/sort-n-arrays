#!/usr/bin/python3

import sys
from random import randint

max_arr_size = 100 # MUST BE BIGGER THEN N
max_value = 100

def gen_sizes(n):	# generate a list of unique sizes
	arr_size = []
	for i in range(0,n):
		k = randint(2, max_arr_size)
		while k in arr_size:
			k = randint(2, max_arr_size)
		arr_size.append(k)
	return arr_size


def gen_array(k):	# generate one array
	one_array = []
	for i in range(0,k):
		one_array.append(randint(-max_value, max_value))
	return one_array

def main():
	n_arrays = []
	arr_size = []	
	k = ''
	
	if len(sys.argv) == 2:	# check if input is digit
		k = sys.argv[1]
	while not k.isdigit():
		print('Please input a number:')
		k = input()
	n = int(k)
	print('n =',n)
	if (n>max_arr_size):	# check that n<max_arr_size
		print('Error! N is bigger then max array size')
		exit()
	
	arr_size = gen_sizes(n)
	print('array sizes:',arr_size)
	
	print('\nGenerated arrays')	
	for i in range(0,n):
		n_arrays.append(gen_array(arr_size[i]))
		print(i,':',n_arrays[i])

	print('\nSorted arrays')
	for i in range(0,n):
		if (i % 2 == 0):
			n_arrays[i].sort()
		else:
			n_arrays[i].sort(reverse=True)
		print(i,':',n_arrays[i])
		
	return n_arrays
	
	
if __name__ == "__main__":
    main()
