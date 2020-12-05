import numpy as np

validEcl = ['amb','blu','brn','gry','grn','hzl','oth']

def checkFields(passport,fields):
    split = passport.split(' ')
    count = 0
    for keyvalues in split:
        if keyvalues == '': break
        key = keyvalues.split(':')[0]
        value = keyvalues.split(':')[1]
        # first task outcommented
        # if fields.count(field) != 0:
        if fields.count(key) != 0 and validateFields(passport,key, value,fields):
            count = count + 1
    if count == len(fields):
        return True
    return False

def validateFields(passport, key,value,fields):
    for f in fields:
        if key == f:
            if key == 'byr':
                return int(value) >= 1920 and int(value) <= 2002
            if key == 'iyr':
                return int(value) >= 2010 and int(value) <= 2020
            if key == 'eyr':
                return int(value) >= 2020 and int(value) <= 2030
            if key == 'hgt':
                array = list(''.join(value.split()))
                i = 0
                for val in array:
                    if val.isnumeric():
                        i = i+1
                h = int(''.join(array[0:i]))
                unit = ''.join(array[i:])
                if unit == 'cm':
                    return int(h) >= 150 and int(h) <= 193
                elif unit == 'in':
                    return int(h) >= 59 and int(h) <= 76
                else:
                    return False
            if key == 'hcl':
                approvedLetters = ['a','b','c','d','e','f']
                array = list(''.join(value.split()))
                if(array[0] != '#'): return False
                if len(array) != 7: return False
                for i,char in enumerate(array):
                    if i == 0: continue
                    c = ''.join(char.split())
                    if c.isalnum() == False:
                        return False
                    if c.isalpha():
                        if approvedLetters.count(c) == 0:
                            return False
                return True
            if key == 'ecl':
                val = ''.join(value.split())
                if validEcl.count(val) == 0:
                    return False
                else:
                    return True
            if key == 'pid':
                val = ''.join(value.split())
                return val.isnumeric() and len(val) == 9

if __name__ == "__main__":
    f = open('/home/fridlund/codeprojects/justforfun/advent-of-code/AOC-4/data/input.in','r')
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    validPassports = 0
    tempPassport = ""
    for line in f.readlines():
        if line != '\n':
            tempPassport = ''.join([tempPassport,line,' '])
        else:
            if checkFields(tempPassport,fields):
                validPassports = validPassports + 1
            tempPassport = ""
    print(validPassports)