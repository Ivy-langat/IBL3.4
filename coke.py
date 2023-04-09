amount_due=50

for _ in range(50):

    print("Amount Due:" , amount_due)

#insert coin
coin=int(input("Insert Coin:"))

if coin in [25,10,5]:

    amount_due -= coin
    

change_owed = abs(amount_due)

print("Change Owed:" , change_owed)
