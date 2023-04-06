def main():
    number= get_number()
    helloworld(number)


def get_number():
            while True:
                x= int(input("enter value of x"))
                if x>0:
                    break
            return x   

def helloworld(n):
    for_ in range(n) 
    print("hello world")  

main()       