import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'E:/SE/project/cheaper/code')
import insertion



#from code import insertion
arr = insertion.insertionSort([4,5,3,1,2])

#checking the length of the returned array
assert(len(arr) == 5)

#check if the returned array is in sorted order
for i in range(1,len(arr)):
    assert(arr[i-1] <= arr[i])

