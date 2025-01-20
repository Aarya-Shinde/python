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
        password = input("\nEnter your PassWord - ");

        confpassword = input("\nEnter your Pass Word again - ");

        if password == confpassword :
                print("Password Matches");
                print("\n Registration Successful");

                database.update({username : password})
                break;
        else :
                print("Password dosen't match");
         
      

    elif move == 2 :
        print('''
        Enter your following Credentials:
        ''');
        username = input("\nEnter your Username - ");
             
        if username in database :
            password = input("Enter your Password: ")
            if database[username] == password :
                  print("Login Sucessfull");
            else :
                  print ("Password dosen't match")
        else :
             print ("Login failed");
        break;
    
    
    else : 
        print("PLEASE TRY AGAIN!!");
         
print(database);