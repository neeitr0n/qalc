import sys
import math

def qalc():

    print("It's a Qalc - Ver. 0.7")
    print("")

    global x,y,z

    def add(x,y):
        print()
        print(f"Result: ",x," + ",y," = ",x+y)
        print()

    def subtract(x,y):
        print()
        print(f"Result: ",x," - ",y," = ",x-y)
        print()

    def multiply(x,y):
        print()
        print(f"Result: ",x," * ",y," = ",x*y)
        print()

    def divide(x,y):
        print()
        print(f"Result: ",x," / ",y," = ",x/y) 
        print()

    def power(x,y):
        print()
        print(f"Result: ",x," ^ ",y," = ",x**y)
        print()

    def root(x):
        print()
        print(f"Result: "," √",x," = ",math.sqrt(x))
        print()

    def factorial(x):
        print()
        print(f"Result: ", x, "!", " =", math.factorial(x))
        print()

    def qes(x,y,z):
        try:
            x = float(input("Input the A - "))
            y = float(input("Input the B - "))
            z = float(input("Input the C - "))
            
            discr = y ** 2 - 4 * x * z 
            print("Discriminant = %.2f" % discr)
            print()

            if discr > 0:
                x1 = (-y + math.sqrt(discr)) / (2*x)
                x2 = (-y - math.sqrt(discr)) / (2*x)
                print("Two real roots:", x1,';', x2, "\n")
            elif discr == 0:
                x3 = -y / (2*x)
                print("Single root:", x3, "\n")
            else:
                print("No real roots (complex solutions exist)\n")
        except ValueError:
            print("Error: Invalid input\n")

    def percentcal(x,y):
        try:
            prcfirnumber = float(input("Enter the first number(main) - "))
            prcact = input("Enter the action(+; -; *; /) - ").strip()
            prcsecnumber = float(input("Enter the second number(percent) - "))
            print() 

            if prcact == "+":
                prcresult = prcfirnumber + prcfirnumber/100*prcsecnumber
                print(f"Result: {prcfirnumber} + {prcsecnumber}% = {prcresult:.2f}\n")
            elif prcact == "-":
                prcresult = prcfirnumber - prcfirnumber/100*prcsecnumber
                print(f"Result: {prcfirnumber} - {prcsecnumber}% = {prcresult:.2f}\n")
            elif prcact == "*":
                prcresult = prcfirnumber * (prcsecnumber / 100)
                print(f"Result: {prcfirnumber} * {prcsecnumber}% = {prcresult:.2f}\n")
            elif prcact == "/":
                if prcsecnumber == 0:
                    print("Error: Division by zero!\n")
                else:
                    prcresult = prcfirnumber / (prcsecnumber / 100)
                    print(f"Result: {prcfirnumber} / {prcsecnumber}% = {prcresult:.2f}\n")
            else:
                print("Invalid Operation!\n")
        except ValueError:
            print("Error: Invalid input\n")
 
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Root")
        print("7. Factorial")
        print("8. Quadratic Equation Solver")
        print("9. Percent Calculator")
        print("0. Exit")

        action = int(input("- "))
        print()

        if action in (1, 2, 3, 4, 5, 6, 7):
            x = int(input("Write first number: "))

            if action not in (6, 7, 9):
                y = int(input("Write second number: "))

        if action == 0:
            break

        if action == 1:
            add(x,y)
         
        if action == 2:
            subtract(x,y)

        if action == 3:
            multiply(x,y)
        
        if action == 4:
            divide(x,y)
        
        if action == 5:
            power(x,y)

        if action == 6:
            root(x)

        if action == 7:
            factorial(x)

        if action == 8:
            qes(0,0,0)

        if action == 9:
            percentcal(0,0)

qalc()
