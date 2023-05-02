import math

def multiply_and_add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = (num1 ** 2) + (num2 ** 2)

    GetSquareRoot = input("Get Sqrt: ")
    if GetSquareRoot in ["y", "yes", "Yes", "Y"]:
        print("The result is:", math.sqrt(result))
    else:
        print("The result is:", result)  
    
    checkContinue()

def checkContinue():
    continueOrQuit = input("Again: ")
    if continueOrQuit in ["y", "yes", "Yes", "Y"]:
        multiply_and_add()

if __name__ == "__main__":
    multiply_and_add()
