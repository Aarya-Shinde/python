'''
print("Welcome to pokemon Gym");
age = int(input("Enter your age"));


if age >= 21 and age < 40 :
    print('You can enroll in our gym');
else: 
  print('sorry, not eligible');

'''
age = int(input("Enter your age"));

if age < 21 or age == 40 :
        print('sorry, not eligible');
elif age > 40 :
  print('sorry, not eligible');
else :
     print('your are eligibe');