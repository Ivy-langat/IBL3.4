def main():
    x= int(input("what is the value of x?"))
    if mod(x):
       print("even")
    else:
        print("odd")

def mod(n):
  # This code is defining a function named `mod` that takes an integer `n` as input. It checks if `n`
  # is divisible by 2 (i.e., if it is an even number) using the modulo operator `%`. If `n` is even,
  # the function returns `True`, otherwise it returns `False`. This function is then called in the
  # `main` function to determine whether the value of `x` entered by the user is even or odd.
    return n % 2 == 0
    

main()