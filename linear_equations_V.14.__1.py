# imports
import random
import time
import os

variable_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# define function_1
def function_1():
    # if 1 negative numbers if 0 positive 
    PosOrNeg = random.randint(0,1)
    if PosOrNeg == 0:
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
        var3 = random.randint(1,100)
    else:
        var1 = random.randint(-100,-1)
        var2 = random.randint(-100,-1)
        var3 = random.randint(-100,-1)
    # shows Q to solve
    print("\nSolve this equation: function_1",var1,random.choice(variable_list),"+",var2,"=",var3)
    # asks user for answer 
    userinput = int(input("\nanswer:"))
        #checking answer
    if userinput == (var3-var2)/var1:
        print("correct:")
    else:
        print("The answer is: function_1 ", (var3-var2)/var1)
# define function_2
def function_2():
    # if 1 negative numbers if 0 positive
    PosOrNeg = random.randint(0,1)
    if PosOrNeg == 0:
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
    else:
        var1 = random.randint(-100,-1)
        var2 = random.randint(-100,-1)
    # shows Q to solve 
    print("\nSolve this equation function_2:",var1,random.choice(variable_list),"=",var2)
    # asks for answer
    userinput = int(input("\nanswer:"))
    # checking answer
    try:
        if userinput==(var1/var2):
            print("correct:")
        else:
            print("The answer is:",(var1/var2))
    except ZeroDivisionError:
        # if divide by 0 do it again 
        function_2()
# defining function_3 
def function_3():
    # if 1 negative numbers if 0 positive
    PosOrNeg = random.randint(0,1)
    if PosOrNeg == 0:
        var1 = random.randint(1,100)
    else:
        var1 = random.randint(-100,-1)
    # shows Q to solve
    print("\nSolve this equation function_3:",random.choice(variable_list),"=",var1)
    # asks for answer
    userinput = int(input("\nanswer:"))
    # checking answer
    try:
        if userinput==(var1):
            print("correct:")
        else:
            print("The answer is:",(var1))
    except ZeroDivisionError:
        # if divide by 0 do it again 
        function_3()
# defining function_4


def function_4():
    # if 1 negative numbers if 0 positive
    PosOrNeg = random.randint(0,1)
    if PosOrNeg == 0:
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
    else:
        var1 = random.randint(-100,-1)
        var2 = random.randint(-100,-1)
    # shows Q to solve
    print("\nSolve this equation function_4:",random.choice(variable_list),"+",var1,"=",var2)
    # asks for answer
    userinput = int(input("\nanswer:"))
    # checking answer
    try:
        if userinput == (var1-var2):
            print("correct:")
        else:
            print("The answer is: ", (var1-var2))
    except ZeroDivisionError:
        # if divide by 0 do it again 
        function_4()


# defining function_5
def function_5():
    # if 1 negative numbers if 0 positive
    PosOrNeg = random.randint(0,1)
    if PosOrNeg == 0:
        var1 = random.randint(1,100)
        var2 = random.randint(1,100)
    else:
        var1 = random.randint(-100,-1)
        var2 = random.randint(-100,-1)
    # shows Q to solve
    print("\nSolve this equation function_5:",random.choice(variable_list),"-",var1,"=",var2)
    # asks for answer
    userinput = int(input("\nanswer:"))
    # checking answer
    try:
        if userinput == (var1+var2):
            print("correct:")
        else:
            print("The answer is: ", (var1+var2))
    except ZeroDivisionError:
        # if divide by 0 do it again 
        function_5()

# function list
fan_list = [function_1,function_2,function_3,function_4,function_5]

#loop
while True:
    # picks a function randomly 
    random.choice(fan_list)()
    time.sleep(3)
    os.system("cls")
