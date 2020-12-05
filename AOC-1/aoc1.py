__package__ = 'src'

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
def partOne(years,target):
    foundEntries = False
    entries = [0,0]
    b = 0
    e = len(years) -1
    
    while foundEntries != True:
        if years[b] + years[e] > target:
            e = e -1
        elif years[b] + years[e] < target:
            b = b +1
        if years[b] + years[e] == target:
            entries = years[b], years[e]
            foundEntries = True
    return entries

 
def partTwo(years,target):
    foundEntries = False
    entries = [0,0,0]
    b = 0
    m = b+1
    e = len(years) -1
    
    while foundEntries != True:
        if years[b] + years[m] + years[e] == target:
            entries = years[b], years[m], years[e]
            return entries
        if years[b] + years[m] +  years[e] > target:
            e = e -1
        elif years[b] + years[m] +  years[e] < target:
            m = m + 1
        if m >= e :
            b = b+1
            if b == len(years): break
            m = b+1
            e = len(years) -1
        # print("b: ",b, "m: ",m,"e: ",e,"length: ",len(years))
    return entries


if __name__ == "__main__":
    f = open('/home/fridlund/codeprojects/justforfun/advent-of-code/AOC-1/data/input.in','r')
    # sortF = open('/home/fridlund/codeprojects/justforfun/advent-of-code/AOC-1/data/sortedInput.in','w')
    years = [int (i) for i in f.readlines()]

    insertionSort(years)
    # sortF.writelines(str(years))
    target = 2020
    ## First part of the puzzle ##
    entries1 = partOne(years,target)
    summ1 = entries1[0] * entries1[1]
    print("First entries: ",entries1, "\nFirst sum: ",summ1)
    ## End of first part ##
    entries2 = partTwo(years,target)
    summ2 = entries2[0] * entries2[1] * entries2[2]
    print("Second entries: ",entries2, "\nSecond sum: ",summ2)

    ## Second part of the puzzle, find 3 numbers ##



    
