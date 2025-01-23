#Problem- take user from user to check if the number is palindrome or not. Revesing the number should be same.

#taking input from user
str1 = input("Enter the String: ");
# Initalizing an empty string to store the reverse value
str2 = " "

# using reverse indexing to print the string in reverse and save it in str2
str2 = (str1[ : : -1]);

print(str2);

# if else statement to check if reversed string matches the original one
if str1 == str2 :
    print(f"Yes, the Number is palindrome");
else :
    print(f"No, the Number is palindrome");