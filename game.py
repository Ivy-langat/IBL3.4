import random
while True:
    try:
        level=int(input("Level: "))
        if level >= 1:
            break

    except:
        pass


random_number = random.randint(1, level)

while True:
    try:
        guess=int(input("Guess: "))
        if guess >= 1:
            if guess < random_number:
                print("too small")
            elif guess > random_number:
                print("too large")
            else:
                print("just right")
                break
    except:
        pass            