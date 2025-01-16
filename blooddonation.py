'''
user wants bloof fonation, 
criteria
if 21 greater age- less than 50
then only ask weight 
   if weight in range of 40- 90 
    donate blood
   else wight is not matching)

else (your age is not matching)    
'''

print("Welcome to blood Donation");

age = int(input('Enter your age: '))

if 21 <= age <= 50:
    weight = float(input("Enter your weigt"))
    if 40 <= weight <= 90:
        print("you can donate blood")
    else:
        print("Sorry your weight is not proper")
else:
    print("Your age is not matching")


