camelCase=input("camelCase:")

print("snake_case:", end="")

#loop
for l in camelCase:

    if l.isupper():
        print("_" + l.lower(), end="")

    else:
        print (l,end="")
        