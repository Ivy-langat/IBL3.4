def main():
    greeting = input ("Greeting: ")
    value= value(greeting)
    print("$" + value)

def value(greeting):
#convert greeting in all lowercase and without whitespaces
    greeting = greeting.lower().strip()

    if greeting[:5]=="hello" :
        return 0

# return $ 20
    elif greeting[0]=="h" :
        return 20

#otherwise input $100
    else:
        return 100

if __name__ == "__main__":
    main()  
