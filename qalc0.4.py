import sys
import math

print("It's a Qalc - Ver. 0.4")
print("")
 
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

    action = input("- ")
    print()

    try:
        acval = int(action)
    except ValueError:
        continue

    if acval == 0:
        sys.exit()

    if acval < 1 or acval > 9:
     sys.exit()

    if acval in (1, 2, 3, 4, 5, 6, 7):
        firstnumber = input("Write first number: ")
        fnval = int(firstnumber)

        if acval not in (6, 7, 9):
            secondnumber = input("Write second number: ")
            snval = int(secondnumber)
     
    if acval == 1:
     print()
     print("Result: ",firstnumber," + ",secondnumber," = ",fnval+snval)
     print()  

    if acval == 2:
     print()
     print("Result: ",firstnumber," - ",secondnumber," = ",fnval-snval)
     print()  

    if acval == 3:
     print()
     print("Result: ",firstnumber," * ",secondnumber," = ",fnval*snval)
     print()  

    if acval == 4:
     print()
     print("Result: ",firstnumber," / ",secondnumber," = ",fnval/snval) 
     print()  

    if acval == 5:
     print()
     print ("Result: ",firstnumber," ^ ",secondnumber," = ",fnval**snval)
     print()  

    if acval == 6:
     print()
     print ("Result: "," √",firstnumber," = ",math.sqrt(fnval))
     print()      
 
    if acval == 7:
     print()
     print("Result: ", firstnumber, "!", " =", math.factorial(fnval))
     print()
	 
    if acval == 8:
     
     aval = input("Input the A - ")
     aval1 = int(aval)

     bval = input("Input the B - ")
     aval2 = int(bval)

     cval = input("Input the C - ")
     aval3 = int(cval)
     
     discr = aval2 ** 2 - 4 * aval1 * aval3 
     print("Discriminant = %.2f" % discr)
     print()

     if discr > 0:
        x1 = (-aval2 + math.sqrt(discr)) / (2*aval1)
        x2 = (-aval2 - math.sqrt(discr)) / (2*aval1)
        print("Two real roots:", x1,';', x2, "\n")
        print()
     elif discr == 0:
        x = -bval / (2*aval)
        print("Single root:", x)
        print()
     else:
        print("No real roots (complex solutions exist)")
        print() 

    if acval == 9:
     
     prcfirnumber = input("Enter the first number(main) -  ")
     prcx = int(prcfirnumber)

     prcact = input("Enter the action(+; -; *; /) -  ")

     prcsecnumber = input("Enter the second number(percent) - ")
     prcxs = int(prcsecnumber)
     print() 

     if prcact == "+":
       prcresult = prcx + prcx/100*prcxs
       print("Result: ",prcx,"+",prcxs,"%","= ",prcresult)
       print() 

     elif prcact == "-":
       prcresult = prcx - prcx/100*prcxs
       print("Result: ",prcx,"-",prcxs,"%","= ",prcresult)
       print() 

     elif prcact == "*":
       prcresult = prcx * (prcxs / 100)
       print("Result: ",prcx,"*",prcxs,"%","= ",prcresult)
       print() 

     elif prcact == "/":
       prcresult = prcx / (prcxs / 100)
       print("Result: ",prcx,"/",prcxs,"%","= ",prcresult)
       print()      

     else:
       print("Invalid Operation!")
       print()    