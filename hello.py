def walking():
    print "You are walking down a lonely road. You approach a fork. \
    Do you go right or left?"
    rchoice = raw_input("\nRight or left? (r/l)\n").lower()
    if rchoice == "r":
        print "You waltze down the right road like you know what you \
        know what you are doing. You slip downhill on a hidden game \
        trail and you realize you are heading to a cliff."
        exclaim1 = raw_input("What do you scream as you head for \
        seemingly certain death?\n").lower()
        print "You yell {0}!!!!".format(exclaim1)
        print "Splat. That was you on the rocks below."
    elif rchoice == "l":
        print "You walk down the road to the left cautiously. Surprise! \
        You find a town that for some reason immediately accepts you as mayor. \
        Good choice on taking the left road."
    else:
        print "You did not make a definitive choice concerning which way to go. You break down and \
        cry. What a baby."
    

def again():
    agChoice = raw_input("Would you like to do more maths? y/n \n")
    if agChoice == "y":
        someMath()
    elif agChoice == "n":
        print "Fine then."
        exit()
    else:
        print "Please use y for yes or n for no."
        again()
        
def someMath():
    opChoice = raw_input("Please enter any of the following to indicate which math operation you would like to do. add, subtract, multiply, or divide. \n")
    if opChoice == "add":
        num1 = raw_input("Please choose your first number")
        num2 = raw_input("Please choose your second number")
        print float(num1) + float(num2)
    elif opChoice == "subtract":
        num1 = raw_input("Please choose your first number")
        num2 = raw_input("Please choose your second number")
        print float(num1) - float(num2)
    elif opChoice == "multiply":
        num1 = raw_input("Please choose your first number")
        num2 = raw_input("Please choose your second number")
        print float(num1) * float(num2)
    elif opChoice == "divide":
        num1 = raw_input("Please choose your first number")
        num2 = raw_input("Please choose your second number")
        print float(num1) / float(num2)
    elif opChoice == "modulus":
        num1 = raw_input("Please choose your first number")
        num2 = raw_input("Please choose your second number")
        print float(num1) % float(num2)
    again()

def counter():
    print "I will count to whatever number you give me (Up to ten)."
    numChoice = raw_input("What number would you like me to count to? Up to ten that is.")
    numlist = [1,2,3,4,5,6,7,8,9,10]
    for number in numlist:
        if number <= float(numChoice):
            print number
    print "Done."

def tupiter():
    tup1 = ("cheese", 5, "rectangle", 89.334)
    for item in tup1:
        print item

def aggCounter():
    numAgg = 0
    while (numAgg < 10):
        numAgg += 1
        print "Counting, currently at: " + str(numAgg) + "."

def logic():
    numb1 = 0
    numb2 = 3
    numb3 = 6
    var3 = False
    numb4 = 9
    numb5 = 2
    if numb2 > numb1 and numb5 > numb1:
        print "true"
    if numb5 > numb3 or numb1 < numb3:
        print "true"
    if not var3: 
        print "tree"

logic()





        
    
        
    
