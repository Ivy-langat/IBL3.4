from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "cookie"
    jar.deposit(4)
    assert str(jar) == "cookiecookiecookiecookiecookie"

def test_deposit():
    jar =Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8

def test_withdraw():
    jar =Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

if __name__ == "__main__":
    main()  