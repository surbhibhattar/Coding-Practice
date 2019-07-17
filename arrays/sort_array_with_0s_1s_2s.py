'''
We want to sort the given array containing 0s 1s and 2s in that order.
One way is to count all the occurrences of 0s, 1s and 2s, and then add them to array one by one.
This runs in O(n) times but we iterate over the array twice.

Another way of solving it is by keeping three pointers in the array - low, mid, high. 
where, low and mid are initially at starting index and high at n-1.
We compare mid element with whether it is zero or one or two. 
If first, we swap with a[low] and a[mid] and increment both low and mid by one.
If second, we do nothing and just increment mid by one.
If third, we swap a[mid] and a[high] and decrement high by one.
We keep doing this until high < mid

This way we can run in O(n) and in place.
'''

def take_input():
    T = int(input())
    for t in range(0, T):
        N = int(input())
        array = list(map(int, input().split()))  
        sorted_array = sort_in_place(array)
        for i in range(0, N):
            print(sorted_array[i], end=' ') # this end = '' is added to avoid printing on a new line
        print() #this empty print is added to get a new line after every test case

def sort(array):
    zeroes = 0
    ones = 0
    twos = 0
    n = len(array)
    for i in range(0, n):
        if array[i] == 0:
            zeroes += 1
        elif array[i] == 1:
            ones += 1
        else:
            twos += 1
    
    sorted_array = []
    curr_index = 0
    for i in range(0, zeroes):
        sorted_array.insert(i, 0)
        curr_index += 1
    for i in range(0, ones):
        sorted_array.insert(curr_index + i, 1)
        curr_index += 1 
    for i in range(0, twos):
        sorted_array.insert(curr_index + i, 2)
    
    return sorted_array
    
# in place solution
def sort_in_place(array):
   low = 0
   mid = 0
   n = len(array)
   high = n - 1
   while mid <= high:
       if array[mid] == 0:
           array[low], array[mid] = array[mid], array[low]
           low += 1
           mid +=1
       elif array[mid] == 1:
           mid +=  1
       else:
           array[high], array[mid] = array[mid], array[high]
           high -= 1
   return array

take_input()
        