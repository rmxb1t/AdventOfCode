import re

def partA():
    result = 0 #define result variable
    with open('input/3_input.txt', 'r') as f: #open file
        file = f.read() #read file
        x = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", file) #find every mul in the string
        #for ele in x: #loop through each finding (list object
            #values = list(map(int, re.findall("\d{1,3}", ele))) #return only the integers, but as type int
            #result += values[0] * values[1] #add up each multiplication result
        result = sum(int(a) * int(b) for a, b in x) #short
    return result #profit

def partB():
    result = 0  # define result variable
    with open('input/3_input.txt', 'r') as f:  # open file
        file = f.read()  # read file
        y = re.sub(r"don\'t\(\).*?do\(\)", "", file, flags=re.DOTALL) #remove every part from don't() - do(), flag ignores \n
        x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", y)  # find every mul in the string
        #for ele in x:  # loop through each finding (list object
            #values = list(map(int, re.findall("\d{1,3}", ele)))  # return only the integers, but as type int
            #result += values[0] * values[1]  # add up each multiplication result
        result = sum(int(a) * int(b) for a, b in x)  # short
    return result  # profit

print("Part A: ", partA())
print("Part B: ", partB())