# To check if the word is an anagram or not. 
# 
# 

# str1 = input("Enter words- ");
# str2 = input("Enter words- ");

str1 = "mad"
str2 = "dam"

flag = True

if len(str1) > len(str2) :

    for i in len(str1) > len(str2) : 

        if i not in str2:
            flag = False;

else :
    for i in str2: 

        if i not in str1:
            flag = False;
   

if flag == True :
  print("It is anagram")

else :
  print("It is not a anagram")
