from collections import deque
import sys

def scan_prev(arr):
    target_sum = arr[-1]

    s = set()
    count = 0
    for i in range(0,len(arr)-1):
        tmp = target_sum-arr[i]
        if tmp in s:
            count = count +1
        s.add(arr[i])
    if count > 0:
        return 0
    else:
        return target_sum

def subarray_sum(arr,target_sum):
    curr_sum = arr[0]
    start = 0
    n = len(arr)
    i = 1

    while i <= n:
        while curr_sum > target_sum and start < i-1:
            curr_sum = curr_sum - arr[start] 
            start += 1
        if curr_sum == target_sum: 
            print ("%d + %d = %d"%(min(arr[start:i]),max(arr[start:i]),max(arr[start:i]) + min(arr[start:i]))) 
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1


def main():
    with open("input.in") as input_file:
        prev_numbers = deque(maxlen=26)
        prev_numbers_list = list()
        for line in input_file:
            prev_numbers.append(int(line))
            prev_numbers_list.append(int(line))
            if(len(prev_numbers) < 26): 
                continue
            num = scan_prev(prev_numbers)
            if num > 0:
                print(num)
                subarray_sum(prev_numbers_list,num)
                
                break
            
                

if __name__ == "__main__":
    main()