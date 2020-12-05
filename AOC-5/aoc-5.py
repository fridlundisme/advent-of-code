import numpy as np

def calculateRow(i,j, arr):
    d = j - i
    if(len(arr) == 1):
        # For seat row
        if arr[0] == 'F':
            return i
        if arr[0] == 'B':
            return j-1
        # For seat column
        if arr[0] == 'L':
            return i
        if arr[0] == 'R':
            return j-1
    b = ''
    e = ''
    # For seat row
    if(arr[0] == 'F'):
        j = j - (d / 2)
    elif(arr[0] == 'B'):
        i = j - (d/ 2)
    
    # For seat column
    if(arr[0] == 'L'):
        j = j - (d / 2)
    elif(arr[0] == 'R'):
        i = j - (d/ 2)
    
    return calculateRow(i,j,arr[1:])



if __name__ == "__main__":
    f = open('/home/fridlund/codeprojects/justforfun/advent-of-code/AOC-5/data/input.in','r')
    highestID = 0
    a = [0]*(127*8+7)
    for line in f.readlines():
      array = list(''.join(line.split()))
      row = calculateRow(0,128,array[:7])
      column = calculateRow(0,8,array[7:])
      ID = int(row * 8 + column)
      a[ID] = 1
      if(ID > highestID):
        highestID = ID

    print("Highest ID: ",highestID)
    
    for i in range(0,highestID):
        if a[i] == 0:
            print(f"ID: {i}")
            print(f"Neighbours ({i-1},{i+1})")