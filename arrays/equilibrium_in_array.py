def take_input():
    T = int(input())
    for t in range(0, T):
        N = int(input())
        array = list(map(int, input().split()))            
        print(find_equilibrium(array))
        
def find_equilibrium(array):
    n = len(array)
    if n == 1:
        return 1
    k = 1
    i = 0
    j = k + 1
    left_sum = array[i]
    right_sum = 0
    for temp in range(j, n):
        right_sum += array[temp]
    for k in range(1, n-1):
        if left_sum == right_sum:
            return k+1
        else:
            left_sum += array[k]
            right_sum -= array[k+1]
    return -1
    
take_input()
