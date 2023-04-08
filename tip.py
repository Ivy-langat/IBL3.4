def main():
    dollar = dollar_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("what percentage would you like to tip?"))
    tip=dollar*percent
    print(f"Leave${tip:.2f}")

def dollar_to_float(d):
    d = float(d.replace("$", ""))
    return d

def percent_to_float(p):
    p = float(p.replace("%", ""))
    p = p/100
    return p

main()
