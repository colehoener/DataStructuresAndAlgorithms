#Mark Boady
#Drexel University
#CS 260 - Summer 2020

#Time Two Sorts
import random
import timeit
def rand_array(size):
	return [random.randint(-2*size,2*size) for n in range(0,size)]
	
def test_a_sort(sort_name,size):
	setup="from sort_code import "+sort_name+"\n"
	setup+="from __main__ import rand_array\n"
	setup+="size="+str(size)+"\n"
	setup+="A=rand_array(size)\n"
	test_code=sort_name+"(A.copy())"
	t=timeit.timeit(test_code,setup,number=1000)
	return t

print("Size | Bubblesort | Insertion Sort | Python sort()")
for x in range(0,11):
	A = rand_array(2**x)
	bt=test_a_sort("bubblesort",2**x)
	it=test_a_sort("insertion",2**x)
	bltins= (timeit.timeit("A.sort()", setup="from __main__ import A")) #Built-in sort() time test
	print("%4d |%11.5f |%11.5f |%11.5f"%(2**x,bt,it, bltins))
