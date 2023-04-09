while True:
    fuel=input("fraction:")

    try:
        num , den= fuel.split("/")
#converting into integer
        new_num=int(num)
        new_den=int(den)

        f=new_num/new_den

        if f<=1:
            break
    except(ValueError, ZeroDivisionError):
        pass

#multiplying percentage
p= int(f*100)

if p<=1:
    print("e")
elif p>=99:
    print("f")
else:
    print(f"{p}%")

