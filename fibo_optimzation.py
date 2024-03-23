import time
from timeit import timeit

import matplotlib
import matplotlib.pyplot as plt
def fib1(n): # example 1 with recurrsion
    if n<=1:
        return 1
    else:
        return fib1(n-2)+fib1(n-1)


def fib2(n): # example 2 without recurrsion
    a=1
    b=1

    for i in range(n):
        a, b =b, a+b
    return a

print('fib1:')

for i in range(15):
    print(fib1(i), end=',  ')



print("\n\n")

print('fib2:')
for i in range(15):
    print(fib2(i), end=",  ")



def computetime(fn, limit): # compute time

    l=[]

    for i in range(limit):
        start_time= round(time.time()*1000)

        fn(i)

        end_time = round(time.time()*1000)

        time_taken=start_time-end_time

        l.append(time_taken)
    return l

limit=30

fib1_times=computetime(fib1,limit)
fib2_times=computetime(fib2,limit)


'''
print(f'\n\nComputing Time for fib1',fib1_times)
print(f'\n\nComputing Time for fib2',fib2_times)
'''

print("\n\n")
print(f'Computing Time for fib1{[abs(x) for x in fib1_times]}')
print("\n\n")
print(f'Computing Time for fib2{[abs(x) for x in fib2_times]}')

timeit(fib1(2))
#matplotlib.interactive()
plt.figure()
plt.xlabel('fib(n')
plt.ylabel('Time (s)')
plt.plot()
plt.plot()
plt.show()


