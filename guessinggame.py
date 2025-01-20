import random

while True :

    print("Welcome to the Guessing Game\n");
    print(''' 
        Choose your level...
            1. Easy  
            2. Meduim  
            3. Hard  ''')
    
    end = 0;
    guess = 0;
    ans = 0;

    level = int(input('Enter your move\n'));

    # If else statement for level selection

    if level == 1 :

        print(f"You have selected easy level   \n");
        end = 30;
        print(ans);

        guess = int(input(f"Guess the no between 1 to {end}: "));
           
        if  guess == ans :
            print ("!!!Congrats that is correct!!");
            break;    
                            
        else : 
            print("Wrong Answer, Try Again");                       

    elif level == 2 :

        print(f"You have selected medium level  \n");
        end = 60;
        print(ans);

        guess = int(input(f"Guess the no between 1 to {end}: "));
           
        if  guess == ans :
            print ("!!!Congrats that is correct!!");
            break;    
                            
        else : 
            print("Wrong Answer, Try Again");
             
        
    elif level == 3 :

        print(f"You have selected hard level  \n");
        end = 100;
        break;
            
    else :
            print("Invalid Input, Please try again!!\n4");

guess = input(f"Guess the no between 1 to {end}: ");

ans = random.randint(1, end);