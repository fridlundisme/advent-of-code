def checkPolicy(line):
    lineArray = line.split(' ')
    # Bad way. Just cast to int when used instead
    # minMaxOccur = list(map(int,lineArray[0].split('-')))
    minMaxOccur = lineArray[0].split('-')
    letter = lineArray[1].split(':')[0]
    password = list(''.join(lineArray[2].split()))

    counter = 0
    for char in password:
        if char == letter:
            counter = counter +1
    if counter <= int(minMaxOccur[1]) and counter >= int(minMaxOccur[0]):
        return True
    return False

def checkSecondPolicy(line):
    lineArray = line.split(' ')
    minMaxOccur = list(map(int,lineArray[0].split('-')))
    i = minMaxOccur[0] -1
    j = minMaxOccur[1] -1
    letter = lineArray[1].split(':')[0]
    password = list(''.join(lineArray[2].split()))

    if (password[i] == letter and password[j] != letter) or  (password[i] != letter and password[j] == letter):
        return True
    return False

if __name__ == "__main__":
    f = open('/home/fridlund/codeprojects/justforfun/advent-of-code/AOC-2/data/input.in','r')
    inputStrings = f.readlines()
    policy1Count = 0
    policy2Count = 0
    for line in inputStrings:
        if checkPolicy(line):
            policy1Count = policy1Count + 1
        if checkSecondPolicy(line):
            policy2Count = policy2Count + 1
    print("Policy 1: ",policy1Count)
    print("Policy 2: ",policy2Count)