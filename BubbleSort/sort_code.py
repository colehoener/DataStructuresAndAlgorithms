#Mark Boady - CS 260
#Drexel University 2020

#Complete the Following Functions
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

def insertion(A):
	for i in range(len(A)):
		value = A[i]
		insertPoint = i

		while insertPoint > 0 and A[insertPoint - 1] > value:
			A[insertPoint] = A[insertPoint - 1]
			insertPoint -= 1
		
		A[insertPoint] = value
	return