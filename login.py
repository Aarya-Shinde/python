'''Creating a user registration and login page'''

database = {"aarya" : "1234"}


while True  : 

    print('''
Enter the Move:
      1. Register 
      2. Login
    ''');

    move = int(input('1 or 2- '));
    
    if move == 1 :
        print('''
        Enter the following Credentials for Registration:
        ''');
        username = input("Enter your Username - ");

        while True :

            password = input("\nEnter your PassWord - ");
            confpassword = input("\nEnter your Pass Word again - ");

            if password == confpassword :
                    print("Password Matches");
                    print("\n Registration Successful");

                    #Updates 

                    database.update({username : password})
                    break;
            else :
                print("Password dosen't match");
         
      

    elif move == 2 :
        print('''
        Enter your following Credentials:
        ''');

        while True :
             
            username = input("\nEnter your Username - ");
                
            if username in database :
                password = input("Enter your Password: ");

                if database[username] == password :
                    print("Login Sucessfull!!!");
                    exit();
                else :
                    print ("Password dosen't match, Please try again!")
            else :
                print("User name dosen't match, Please Try again!")
    else :
        print ("Login failed, PLEASE TRY AGAIN!!");
        
         
print(database);