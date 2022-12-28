import random
import time
random.seed(time.time())
'''
As we have to print the box together(The rows in the box must print below each other) 

>>>I first printed all the first rows in the box1,2,3 in level 1 then the secon and the third<<<

This is why the loop order is i,j,k but the order at print of the list is i,k,j
'''
def display():# to display the list
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(a[i][k][j],end="")
            print()
        print()
def col_check():# To see that there are no element similar to the given element in that coloum
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if a[i][box][k][element]==test_dig:
                    return False
    return True
def row_check():# To see that there are no element similar to the given element in that row
    for i in range(3):
        for j in range(3):
            if a[level][i][row][j]==test_dig:
                return False
    return True
            
def box_check():# To see that there are no element similar to the given element in that box
    for i in range(3):
        for j in range(3):
            if a[level][box][j][i]==test_dig :
                return False
    return True

a=[[[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]]
possible=[1,2,3,4,5,6,7,8,9]# The numbers which are can be added to the board
run =True
test_dig=0
turn_case=0
level=0 # Theere are three level
box=0 # There are three boxes per level
row=0 # There are three rows per box
element=0
fac=[True,False,True,False]
time_run=0
while level<3:
    while  box < 3:
        while row < 3:
            while element < 3:
                while run:
                    time_run+=1 # To know how many times the main loop has run
                    test_dig+=1 # The number to be inserted is being incremented
                    if fac[random.randint(0,3)]:# To not get the numbers in and order we are adding some randomness
                        test_dig+=1
                    if test_dig>9:# As the number greater than 9 can not be inserted in the board
                        test_dig=1
                    if row_check() and col_check() and box_check() :#To check the conditions
                        a[level][box][row][element]=test_dig
                        run=False # After entering the we must go to next element so the innermost loop must be terminated
                        turn_case=0
                    turn_case+=1
                    if turn_case==100:# Some times due to randomness, any number can not be entered to the position so we must start from the beigning,<<100 is a arbitrary number which i felt was working good for me>>
                        a=[[[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]]
                        level=0
                        box=0
                        row=0
                        element=0
                        test_dig=0
                        turn_case=0
                run=True
                element+=1 
            row+=1
            element=0
        box+=1
        row=0
    box=0
    level+=1
display()
print(time_run)# To see how many times the main loop has run>>>The lowest i got is 1951<<<