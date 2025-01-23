# Add Numbers entered by the user-
# eg ---  23-->5
#         1234-->10

num = int(input("Enter the Number: "));

result = 0;

for i in str(num) :
    result += int(i);
    print(f"Value of result is now: {result}")

print(result);