import timeit
from josephus_functions import josephus_list
from josephus_functions import josephus_deque
print("Using M=2 and Number=? in timeit")
print("Size |  List Ver  | Dequeue Ver|")

for x in range(0,11):
    lt = timeit.timeit("josephus_list(2**x, 2)", setup="from __main__ import josephus_list, x")
    dqt = timeit.timeit("josephus_deque(2**x, 2)", setup="from __main__ import josephus_deque, x")

    print("%4d |%11.5f |%11.5f |"%(2**x,lt, dqt))