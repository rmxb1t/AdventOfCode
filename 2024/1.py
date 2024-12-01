def partA():
    arrOne = [] #define array one
    arrTwo = [] #define array two
    distance = 0 #varibale to keep track of the distance
    with open("1_input.txt", "r") as file: #open input file as file
        for line in file: #iterate through each line of the file
            arrOne.append(line[:5]) #cut away everything of the output besides the first 5 literals
            arrTwo.append(line[5:]) #cut away everything of the output besides the last 5 literals
    #sort both arrays
    arrOne.sort()
    arrTwo.sort()

    for i in range(len(arrOne)): #calculate the absolute difference between both literals
        distance += abs(int(arrOne[i]) - int(arrTwo[i]))

    return distance

def partB():
    arrOne = []  # define array one
    arrTwo = []  # define array two
    result = 0 #initialise the result
    with open("1_input.txt", "r") as file:  # open input file as file
        for line in file:  # iterate through each line of the file
            arrOne.append(line[:5])  # cut away everything of the output besides the first 5 literals
            arrTwo.append(line[5:])  # cut away everything of the output besides the last 5 literals
    # sort both arrays
    arrOne.sort()
    arrTwo.sort()

    for i in range(len(arrOne)): #iterate over the first array
        count = 0 #reset count after every iteration of the first array
        for j in range(len(arrTwo)): #iterate over the second array
            if int(arrOne[i]) == int(arrTwo[j]):
                count+=1 #increment the counter if the number of the left list appears in the right list
        tmp = int(arrOne[i])
        tmpresult = tmp * count #multiply the number by findings
        result += tmpresult #add every multiplication together to have the result

    return result

print(partA())
print(partB())