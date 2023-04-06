Greeting = input ("Greeting: ")

#convert greeting in all lowercase and without whitespaces
Greeting = Greeting.lower().strip()

if Greeting[0:5]=="hello" :
    print("$0")

# return $ 20
elif Greeting[0]=="h" :
        print("$20")

#otherwise input $100
else:
            print("$100")

