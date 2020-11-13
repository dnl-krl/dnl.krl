import random

def names():
    name = open('names.txt', 'r')
    result = []
    for line in name.readlines():
        r_name = line.split()[1]
        result.append(r_name)
    print(result)

result = names()

#############################################

def names():
    name = open('domains.txt', 'r')
    result = []
    for line in name.readlines():
        line = line.rstrip()
        result.append(line[1::])
    print(result)

result = names()

#############################################
