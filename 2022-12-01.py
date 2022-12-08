import os
maxcalories=0
currentcalories=0

my_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '2022-12-01_input.txt')

with open(my_file) as file:
    for item in file:
        if item!='\n':
            currentcalories+=int(item)
        else:
            if currentcalories>maxcalories:
                maxcalories=currentcalories
            currentcalories=0
print(maxcalories)