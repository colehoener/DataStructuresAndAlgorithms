#Based on Pseudocode by Mark Boady - CS 260
#Drexel University 2020
#
#Converted to code by Cole Hoener

import math

#Basic Swap function
def swap(a, b):
	temp = a
	a = b
	b = temp

	return a,b

#Bubble Sort
def bubblesort(A):
	isSorted = False
	while isSorted == False:
		isSorted = True
		for i in range(len(A) - 1):
			if A[i] > A[i + 1]:
				temp = A[i]
				A[i] = A[i+1]
				A[i+1] = temp
				isSorted = False

	return

#Insertion Sort
def insertion(A):
	for i in range(len(A)):
		value = A[i]
		insertPoint = i

		while insertPoint > 0 and A[insertPoint - 1] > value:
			A[insertPoint] = A[insertPoint - 1]
			insertPoint -= 1
		
		A[insertPoint] = value
	return

#Merge Sort
def merge(A, start, middle, stop):
	Aux = A[start:stop+1]
	Aux_middle = middle - start
	Aux_stop = stop - start
	i = 0
	j = Aux_middle+1

	for k in range(start, stop+1):
		if i > Aux_middle:
			A[k] = Aux[j]
			j+=1
		elif j > Aux_stop:
			A[k] = Aux[i]
			i+=1
		elif Aux[j] > Aux[i]:
			A[k] = Aux[i]
			i+=1
		else:
			A[k] = Aux[j]
			j+=1

	return

def mergesort(A, size):
	msort(A, 0, size - 1)

def msort(A, start, stop):
	if start >= stop:
		return
	
	middle = start + math.floor((stop - start) / 2)
	msort(A, start, middle)
	msort(A, middle+1, stop)
	merge(A, start, middle, stop)

	return

#Quick Sort
def partition(A, start, stop):
	pivot = A[stop]
	i = start
	for j in range(start, stop):
		if A[j] <= pivot:
			A[i], A[j] = swap(A[i], A[j])
			i+=1
		
	A[i], A[stop] = swap(A[i], A[stop])
	return i

def quicksort(A, size):
	qsort(A, 0, size - 1)


def qsort(A, start, stop):
	if start < stop:
		p = partition(A, start, stop)
		qsort(A, start, p-1)
		qsort(A, p+1, stop)
	
