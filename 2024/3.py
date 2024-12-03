import re

def partA():
    result = 0 #define result variable
    with open('3_input.txt', 'r') as f: #open file
        file = f.read() #read file
        x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", file) #find every mul in the string
        for ele in x: #loop through each finding (list object
            values = list(map(int, re.findall("[0-9]{1,3}", ele))) #return only the integers, but as type int
            result += values[0] * values[1] #add up each multiplication result
    return result #profit

def partB():

    return
print(partA())
partB()