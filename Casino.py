import random
import sys

def checkCash(cash):
    if cash < 10000:
        print("Can't play the game")
        return False
    else:
        print("Can play the game")
        return True

def checkAge(age):
    if age < 18:
        print("You can't play the game as you are underage")
        return False 
    else:
        print("You are eligible")
        return True

def checkNum(x):
    if(x>=1 and x<=30):
        return True
    else:
        return False
    
def printResult(cash):
    print(f"Thanks for playing, you are left with Rs {cash}")

def gameFunction(cash):
    while cash > 3000:
        n = int(input("Enter a number between 1 to 30: "))
        x = random.randint(1, 30)
        
        if not checkNum(n):
            print("Not thats not in range try again")
            gameFunction(cash)
        if n == x:
            cash += 5000
            print("Congratulations! You won Rs 5000!")
        else:
            cash -= 2000
            print("Sorry, you lost Rs 2000.")

        if cash <= 3000:
            print("You can't go below Rs 3000.")
            con = input("Do you want to continue? (y/n): ")
            if con == 'y':
                c = int(input("Please enter cash amount above Rs 10,000: "))
                if c >= 10000:
                    cash += c
                else:
                    print("Insufficient cash to continue.")
                    printResult(cash)
                    return
            else:
                printResult(cash)
                return

    printResult(cash)


# Main program
name = input("Please enter your name: ")

age = int(input("Please enter your age: "))
if not checkAge(age):  # If underage, exit the program
    sys.exit()  # Properly exit the program

cash = float(input("Please enter the cash: "))
if not checkCash(cash):  # If cash is less than 10,000, exit the program
    sys.exit()  # Properly exit the program

gameFunction(cash)  # Call the game function if all checks are passed
