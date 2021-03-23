'''
### https://www.youtube.com/watch?v=rfscVS0vtbw

## working with strings

character_name = "Galab"
age ="70"
print("My name is " + character_name + "")
print("I am " + age + "")
print("I like to party\nI am a party goer")
system = "GALAB"
print(system.islower())
print(system[1])
print(system.index("G"))
print(system.replace("G","S"))


## working with numbers
from math import *
print(2-40-20+45)
print(10%3)# modulus operations
mynum =  -5
print(str(abs(mynum)) + " is my fav number") # string and number concatenation
print(pow(3,4))# raising the power of a number
print(min(3,5))
print(round(3.56,1))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(25))
'''

##  displaying the max and min
list = []

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    
    try:
        
    	num = int(num)
        list.append(num)
        
    except: 
        
        print("Invalid input")
        continue
            
       
print("Maximum is", max(list))
print("Minimum is", min(list))