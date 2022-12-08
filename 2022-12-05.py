import os

stack1 = ["W","D", "G", "B", "H", "R", "V"]
stack2 = ["J","N", "G", "C", "R", "F"] 
stack3 = ["L","S", "F", "H", "D", "N", "J"] 
stack4 = ["J","D", "S", "V"]
stack5 = ["S", "H", "D", "R", "Q", "W", "N", "V"]
stack6 = ["P", "G", "H", "C", "M"]
stack7 = ["F", "J", "B", "G", "L", "Z", "H", "C"]
stack8 = ["S", "J", "R"]
stack9 = ["L", "G", "S", "R", "B", "N", "V", "M"]
ship = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

my_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '2022-12-05_input.txt')
with open(my_file) as file:
    for item in file:
        row = item.split(' ')
        for x in range (int(row[1])):
            ship[int(row[5])-1].append(ship[int(row[3])-1][len(ship[int(row[3])-1])-1])
            del ship[int(row[3])-1][len(ship[int(row[3])-1])-1]
for x in range(9):
    print(ship[x][len(ship[x])-1], end='')