import  random

a = True

tahminPC = random.randint(0,100)

while(a==True):
    UserGues = int(input("Enter your gues :   "))
    if(UserGues == tahminPC):
        print("Correct guess")
        break
    else:
        print("Wrong guess")

    if(UserGues<tahminPC-20):
        print("Your guess too small")
        continue
    elif(UserGues<tahminPC):
        print("Your guess small")
    elif(UserGues>tahminPC+20):
        print("You guess too big!")
        continue
    else:
        print("You guess big!")
