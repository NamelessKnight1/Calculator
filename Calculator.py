
def Addition(num1, num2):
    return num1+num2
def Substract( num1, num2):
    return num1-num2
def Multiply(num1, num2):
    return num1*num2   
def Division(num1, num2 ):
    return num1/num2



while True:
    num1= float(input("Enter your first number: "))
    

    print("Press 1 for Addition\nPress 2 for subtraction\nPress 3 for Multiplication\nPress 4 for Division")
    
    
    options = ["1", "2", "3" ,"4", "Q", "q"]
     
    choice = input("Enter your operator: ")
   
    if choice not in options:
        print("Invalid operator")
        continue

    num2= float(input("Enter your second number: "))

    if choice == "1":
        print(Addition(num1, num2))
    elif choice == "2":
        print(Substract(num1, num2))    
    elif choice == "3":
        print(Multiply(num1, num2))
    elif choice == "4":
        print(Division(num1, num2))
    Again = input("Do u want to calculate agin? YES/NO\n")
    if Again == "YES".lower():
            continue
    else:
            print("thanks")
            exit()

    
    



