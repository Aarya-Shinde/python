'''
given_time = float(input());
print(f"You have entered {given_time}");

if (6 <= given_time and given_time <= 12) or (6 <= given_time and given_time <= 12) :
    print("Good Morning");
elif (1 <= given_time and given_time <= 5) or (20 <= given_time and given_time <= 24)  :
    print("Good Night");
elif (1 <= given_time and given_time <= 5) or (13 <= given_time and given_time <= 17)  :
    print("Good Afternoon");   
elif (6 <= given_time and given_time <= 8) or (18 <= given_time and given_time <= 20)  :
    print("Good Evening");    
    

else :
    print("Envalid Input");

'''

given_time = float(input());
print(f"You have entered {given_time}");

if given_time >= 6 and given_time <=12 :
    print("Good Morning");
elif given_time >=13 and given_time <=16 :
    print("Good Afternoon");
elif given_time >= 17 and given_time <= 19:
    print("Good Evening");
elif given_time >= 20 and given_time <=24  or given_time >=1 and given_time <=5 :   
    print("Good Night");
else :
    print("Envalid Input");
