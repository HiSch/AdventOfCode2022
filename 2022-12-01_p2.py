import os
elves=[]
currentcalories=0

my_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '2022-12-01_input.txt')

with open(my_file) as file:
    for item in file:
        if item!='\n':
            currentcalories+=int(item)
        else:
            elves.append(currentcalories)
            currentcalories=0
elves.sort()
sumofcalories = elves[len(elves)-1]+elves[len(elves)-2]+elves[len(elves)-3]
print(sumofcalories)