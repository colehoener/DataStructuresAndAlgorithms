#Mark Boady
#Drexel University
#CS 260 - Summer 2020

#This function generate a random list of
#size
#It sorts using the given sort_fun
#It then checks that the answer is correct
import random

def check_list(sort_fun,size):
	X=[random.randint(-10*size,10*size) for n in range(0,size)]
	T=X[:]#Make a copy
	sort_fun(T)
	#Is the array sorted?
	for i in range(1,len(T)):
		assert T[i] >= T[i-1]
	#Are all the elements in the list?
	for num in X:
		assert T.count(num)==X.count(num)
	return

def check_list_with_size(sort_fun,size):
	X=[random.randint(-10*size,10*size) for n in range(0,size)]
	T=X[:]#Make a copy
	sort_fun(T, size)
	#Is the array sorted?
	for i in range(1,len(T)):
		assert T[i] >= T[i-1]
	#Are all the elements in the list?
	for num in X:
		assert T.count(num)==X.count(num)
	return
	
import sort_code

#Bubble Sort Versions
def test_bubble_ten():
	check_list(sort_code.bubblesort,10)
def test_bubble_hundred():
	check_list(sort_code.bubblesort,100)
def test_bubble_thousand():
	check_list(sort_code.bubblesort,1000)
def test_bubble_fivethousand():
	check_list(sort_code.bubblesort,5000)

#Insertion Sort Version
def test_insert_ten():
	check_list(sort_code.insertion,10)
def test_insert_hundred():
	check_list(sort_code.insertion,100)
def test_insert_thousand():
	check_list(sort_code.insertion,1000)
def test_insert_fivethousand():
	check_list(sort_code.insertion,5000)

#Merge Sort Version
def test_mergesort_ten():
	check_list_with_size(sort_code.mergesort,10)
def test_mergesort_hundred():
	check_list_with_size(sort_code.mergesort,100)
def test_mergesortt_thousand():
	check_list_with_size(sort_code.mergesort,1000)
def test_mergesort_fivethousand():
	check_list_with_size(sort_code.mergesort,5000)

#Quick Sort Version
def test_quicksort_ten():
	check_list_with_size(sort_code.quicksort,10)
def test_quicksort_hundred():
	check_list_with_size(sort_code.quicksort,100)
def test_quicksort_thousand():
	check_list_with_size(sort_code.quicksort,1000)
def test_quicksort_fivethousand():
	check_list_with_size(sort_code.quicksort,5000)

