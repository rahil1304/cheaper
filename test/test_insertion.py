# import code.insertion
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'code')))
from code.insertion import *
arr = insertionSort([4,5,3,1,2])

def test_sort():
    assert (check_sort(arr) and check_length(arr))

#check if the returned array is in sorted order
def check_sort(l):
    flag = 1
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            flag = 0
    return flag

#checking the length of the returned array
def check_length(l):
    return len(l) == 5