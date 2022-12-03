sum1 = 0
sum2= 0

with open("day_2.txt") as f: #read input data
    lines = f.readlines()

# first row is my opponent
# A = Rock
# B = Paper
# C = Scissors

# second row is mine
# X = Rock +1
# Y = Paper +2
# Z = Scissors +3

# total score = Sum of scores of each round
# round score = 1 for Rock, 2 for Paper, and 3 for Scissors
# + outcome: 0 = loss, 3 = draw, 6 = win

for i in range(len(lines)): #loop over every row
    if "A X" in lines[i]: #check if <> is in the current row
        sum1 += 4 # chose Rock and Draw (1+3)
    elif "A Y" in lines[i]:
        sum1 += 8 # chose paper and won (2+6)
    elif "A Z" in lines[i]:
        sum1 += 3 # chose scissors and lost (0+3)
    elif "B X" in lines[i]:
        sum1 += 1 # chose Rock and lost (1+0)
    elif "B Y" in lines[i]:
        sum1 += 5 # chose paper and draw (2+3)
    elif "B Z" in lines[i]:
        sum1 += 9 # chose scissors and won (3+6)
    elif "C X" in lines[i]:
        sum1 += 7 # chose rock and won (1+6)
    elif "C Y" in lines[i]:
        sum1 += 2 # chose paper and lost (2+0)
    elif "C Z" in lines[i]:
        sum1 += 6 # chose scissors and draw (3+3)


print(sum1) #print result

for i in range(len(lines)): #loop over every row
    if "A X" in lines[i]: #check if <> is in the current row
        sum2 += 3 # chose scissors and lose (0+3)
    elif "A Y" in lines[i]:
        sum2 += 4 # chose rock and draw (1+3)
    elif "A Z" in lines[i]:
        sum2 += 8 # chose scissors and lost (2+6)
    elif "B X" in lines[i]:
        sum2 += 1  # chose Rock and lost (1+0)
    elif "B Y" in lines[i]:
        sum2 += 5  # chose paper and draw (2+3)
    elif "B Z" in lines[i]:
        sum2 += 9  # chose scissors and won (3+6)
    elif "C X" in lines[i]:
        sum2 += 2  # chose paper and lost (2+0)
    elif "C Y" in lines[i]:
        sum2 += 6  # chose scissors and draw (3+3)
    elif "C Z" in lines[i]:
        sum2 += 7  # chose rock and won (1+6)

print(sum2) #print result