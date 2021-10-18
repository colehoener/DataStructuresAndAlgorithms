import timeit
from powFuncs import pow1, pow2, pow3 

i = 1

#Start of main execution
if __name__ == '__main__':
    #POW1 TIMES
    print("pow1 Times")
    while i <= 10000:
        print("b= %.0f  Time(ms)= %.3f" % (i, (1000*(timeit.timeit("pow1(9, i)", setup="from __main__ import pow1, i")))))
        i = i * 10
    print()

    #POW 2 TIMES
    print("pow2 Times")
    i = 1
    while i <= 10000:
        print("b= %.0f  Time(ms)= %.3f" % (i, (1000*(timeit.timeit("pow1(9, i)", setup="from __main__ import pow1, i")))))
        i = i * 10
    print()

    #POW 3 TIMES
    print("pow3 Times")
    i = 1
    while i <= 10000:
        print("b= %.0f  Time(ms)= %.3f" % (i, (1000*(timeit.timeit("pow1(9, i)", setup="from __main__ import pow1, i")))))
        i = i * 10
