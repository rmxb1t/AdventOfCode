def partA():
    with open('2_input.txt', 'r') as f: #open file
        content = f.read().strip().split('\n') #read the file

    ans = 0 #result
    for report in content: #iterate over each line in the file
        values = list(map(int, report.split())) #split up each object into a seperate list and convert every element into int
        safepos = set([1, 2, 3]) #define a set (no duplicates allowed) for safepos
        safeneg = set([-1, -2, -3]) #define a set (no duplicates allowed) for safepos
        for i in range(1, len(values)): #iterate through values
            safepos.add(values[i] - values[i - 1]) #add difference of both numbers, if not steps 1-3, "skip"
            safeneg.add(values[i] - values[i - 1])

        if len(safepos) == 3 or len(safeneg) == 3: #if steps are correct
            ans += 1 #increment answer

    print(ans)


partA()
