import sys

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

firstnumber = input("write a first number: ")
fnval = int(firstnumber)

secondnumber = input("write a second number: ")
snval = int(secondnumber)

action = input("write a needable action(1=plus, 2=minus, 3=multiply, 4=divide):  ")     
acval = int(action)

if acval == 1:
    print(firstnumber," + ",secondnumber," = ",fnval+snval)

if acval == 2:
    print(firstnumber," - ",secondnumber," = ",fnval-snval)

if acval == 3:
    print(firstnumber," * ",secondnumber," = ",fnval*snval)

if acval == 4:
    print(firstnumber," / ",secondnumber," = ",fnval/snval)            
