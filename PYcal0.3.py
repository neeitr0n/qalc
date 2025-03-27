import sys
import math

print("it's a PYcal(PYthoncalculator) ver: 0.3a")
print("")
 
while True:
 print("Select operation:")
 print("1. Add")
 print("2. Subtract")
 print("3. Multiply")
 print("4. Divide")
 print("5. Power")
 print("6. Root")
 print("0. Exit")

 action = input("- ")     
 acval = int(action)

 if acval < 1 or acval > 6:
     sys.exit()

 firstnumber = input("Write a first number: ")
 fnval = int(firstnumber)

 if acval != 6: 
     secondnumber = input("Write the second number: ")
     snval = float(secondnumber)


 if acval == 1:
     print("Result: ",firstnumber," + ",secondnumber," = ",fnval+snval)
     print("")  

 if acval == 2:
     print("Result: ",firstnumber," - ",secondnumber," = ",fnval-snval)
     print("")  

 if acval == 3:
     print("Result: ",firstnumber," * ",secondnumber," = ",fnval*snval)
     print("")  

 if acval == 4:
     print("Result: ",firstnumber," / ",secondnumber," = ",fnval/snval) 
     print("")  

 if acval == 5:
     print ("Result: ",firstnumber," ^ ",secondnumber," = ",fnval**snval)
     print("")  

 if acval == 6:
     print ("Result: "," √",firstnumber," = ",math.sqrt(fnval))
     print("")             

if acval ==0:
    sys.exit()
