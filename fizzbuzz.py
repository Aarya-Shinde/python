# Print 1 to 100, then---

# if no is divisibe by 3, the print "Fizz"
# if no is divisibe by 5, the print "Buzz"
# if no is divisibe by 3 and 5, the print "Fizz Buzz"

# easy Method---------

for i in range(1 , 101) :

    if i%3 == 0 and i%5 == 0:
         print (f"Fizz Buzz ");
    
    elif  i%3 == 0 :
        print("Fizz");
    
    elif i%5 == 0 :
        print("Buzz"); 
    
    else :
        print(i);





# Hard method------

# for i in range(1 , 101) :

#     both1 = False
#     both2 = False

#     if both1 == True and both2 == True:
#          print (f" Fizz Buzz ");
    
#     if  i%3 == 0 :
#         both1 = True
#         print("Fizz");
    
#     elif i%5 == 0 :
#         both2 =True
#         print("Buzz"); 
    
#     else :
#         print(i);


