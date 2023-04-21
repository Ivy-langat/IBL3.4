def main():
    fraction = input("Fraction")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            num , den= fraction.split("/")
#converting into integer
            new_num=int(num)
            new_den=int(den)

            f=new_num/new_den

            if f<=1:
                p= int(f*100)
                return p
            else:
                fraction =input("Fraction")
                pass
        except(ValueError, ZeroDivisionError):
            raise

#multiplying percentage
def gauge(p):

    if p<=1:
        return "e"
    elif p>=99:
        return "f"
    else:
        return str(p) + "%"

if __name__ =="__main__":
    main()
