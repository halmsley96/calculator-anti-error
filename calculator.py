#print("My first simple calculator, anti ERROR ! \n")

#My goal is to fix any error if the user input is not number or symbol and of course a working calculator ;P

info = ["Subtract(-)", "Divided(/)", "Addition(+)", "Multiply(x)"]
print(info)

while True: #This will ask the user tu input again and again if the user is idiot :P #loop

    num1 = input("Enter a number : ")

    if num1.isnumeric(): #change from str to int
        num1 = int(num1)
        pass #once it become int it pass to next task

    else:
        print("Invalid, Try again !") #anti error ! will ask the user again to put number
        continue #asking the num1 task again

    num2 = input("Enter a second number : ")

    if num2.isnumeric():
        num2 = int(num2)
        pass

    else:
        print("Invalid, Try again !")
        continue

    sym = input("Enter a operator : ")

    #make the user input ( str to operator )
    if sym == "+":
        result = num1 + num2

    elif sym == "-":
        result = num1 - num2

    elif sym == "x":
        result = num1 * num2

    elif sym == "/":
        result = num1/num2

    else:
        print("Invalid, Try again !")
        continue

    print("The answer is", result)
    break #to finish the masterpiece, if i dont put this it will ask the user again num1 task

