#Mark Boady CS 260 - Drexel University 2020
from collections import deque

#Josephus
#Implemented using the builtin list as the queue
def josephus_list(n,m):
	results=[]
	Q = []
	
	#Fills Q with each person in order (0 to n)
	for i in range(0, n):
		Q.append(i)

	#Executes until Q i empty
	while not(len(Q)==0):
		#Runs through every m people.
		for i in range(0, m):
			#If person is not mth person, adds to end of queue Q
			#Else, "kills" person and appends to result while removing from Q
			if (i < m - 1):
				Q.append(Q.pop(0))
			else:
				results.append(Q.pop(0))
		
	return results
	
#Implemented using the deque object from collections
def josephus_deque(n,m):
	results=[]

	Q = deque()

	#Fills Q with each person in order (0 to n)
	for i in range(0, n):
		Q.append(i)

	#Executes until Q i empty
	while len(Q)!=0:
		#Runs through every m people.
		for i in range(0, m):
			#If person is not mth person, adds to end of queue Q
			#Else, "kills" person and appends to result while removing from Q
			if(i < m - 1):
				Q.append(Q.popleft())
			else:
				results.append(Q.popleft())

	return results