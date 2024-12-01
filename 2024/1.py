arrOne = []
arrTwo = []
# define two arrays
def myfunction():
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

    file.close() #close the opened file :)
    return distance

print(myfunction())