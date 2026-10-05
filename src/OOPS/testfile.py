import Calculator

def getdata():
    a,b=0,1
    while a<1000:
        print(a,end=",")
        a,b=b,a+b

def printinouts(username,*empdetails,**projects):
    print("Name of the employee: ", username)
    for x in empdetails:
        print("details:",x)
    for x in projects:
        print(x,":", projects[x])


cal=Calculator.clc.add(12,12)
print(cal)

#printinouts("Varun Sharma","45","20//11//1981","Male",Locaiton="Kolkata",company="LTM")
#import sys
#print("total arguments passed :" , len(sys.argv)-1)
#print("All arguments :" , sys.argv)
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", required=True)
parser.add_argument("--age", type=int, required=True)

args = parser.parse_args()

print("Name:", args.name)
print("Age:", args.age)

"""

#print("Argument 0 is " + sys.argv[0])

#print("Argument 1 is " + sys.argv[1])

#print("Argument 2 is " + sys.argv[2])

#print(sys.argv.)
#try:
#    print("Argument 2 is " + sys.argv[3])
#except:
#    print("Error : Argument 3 not found")


