# Reverse print from 100 to 1;

# i= 100
# while i>= 1:
#     print(i);
#     i -= 1;

# print("Enter the number you want table of-")
# num = input();
# type(num)

# i = 1
# while i <= 10 :
#     print(num * i );
#     i += 1;


'''
print table for given number.
Enter the number you want table of-
4
4 * 1  = 4
4 * 2  = 8
4 * 3  = 12
4 * 4  = 16
4 * 5  = 20
4 * 6  = 24
4 * 7  = 28
4 * 8  = 32
4 * 9  = 36
4 * 10  = 40    
'''

print("Enter the number you want table of-")
multiple = int(input());

i = 1;
while i <= 10 :
    print(f"{multiple} * {i}  = {multiple*i}");
    i += 1;


