import sys
import math

print("it's a pycal(pythoncalculator) ver: 0.1a")
print("|")
firstquestion = input("wanna to start?(1-y; 2-n): ")
fqval = int(firstquestion)

if fqval == 2:
    sys.exit()

if fqval > 2:
    sys.exit()

if fqval < 1:
    sys.exit()

if fqval == 1:
    print("")   

print("write a required action")
print("1=plus")
print("2=minus")
print("3=multiply")
print("4=divide")
print("5=raise to the power")
print("6=square root")

action = input("- ")     
acval = int(action)

if acval < 1 or acval > 6:
    sys.exit()

firstnumber = input("write a first number: ")
fnval = int(firstnumber)

if acval != 6: 
    secondnumber = input("Write the second number: ")
    snval = float(secondnumber)


if acval == 1:
    print(firstnumber," + ",secondnumber," = ",fnval+snval)

if acval == 2:
    print(firstnumber," - ",secondnumber," = ",fnval-snval)

if acval == 3:
    print(firstnumber," * ",secondnumber," = ",fnval*snval)

if acval == 4:
    print(firstnumber," / ",secondnumber," = ",fnval/snval) 

if acval == 5:
    print (firstnumber," ^ ",secondnumber," = ",fnval**snval)

if acval == 6:
    print (" √",firstnumber," = ",math.sqrt(fnval))             
