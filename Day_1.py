ergebnisliste = []
schleife = 0

with open ("input_data.txt") as f:
    lines = f.readlines()

for x in range(len(lines)):
    lines[x] = lines[x][:-1]
    if lines[x] != '':
        schleife+=int(lines[x])
    else:
        ergebnisliste.append(schleife)
        schleife = 0
ergebnisliste.sort()
ergebnisliste.reverse()

#Ergebnis Part 1
print(ergebnisliste[0])

#Ergebnis Part 2
sum = ergebnisliste[0]+ergebnisliste[1]+ergebnisliste[2]
print(sum)