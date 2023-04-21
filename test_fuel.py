from fuel import convert, gauge
import pytest

def main():
    #calling the test functions
    test_correct_input()
    test_zero_division_error()
#test ZeroDivisionError
def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
#test correct input
def test_correct_input():
    assert convert("1/4")== 25 and gauge(25)== "25%"
    assert convert("99/100")== 99 and gauge(99)== "f"

if __name__ == "__main__":
    main()  