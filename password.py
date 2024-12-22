password={"martin":"martins","mariella":"username","thomas":"scvhool"}
x=password.keys()
y=password.values()
user=input("pls enter the username")
if user in x:
    password1=input('correct please enter the password')
    #print(password[key])
    if password[user] == password1:
        print ('correct youre in')
    else:
        print('incoreect password,acces denied')
else:
    print('incorrect username')