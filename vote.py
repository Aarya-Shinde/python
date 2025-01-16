print('Enter your credentials please');
name = input("Enter your name ");
age = int(input("Enter your age"));

if age >= 18 :
  print( f"Yes you can vote {name}");
elif age <18 :
  print(f"sorry , you have to wait, {18 - age} years");
else:
  print(f"You have to wait...");